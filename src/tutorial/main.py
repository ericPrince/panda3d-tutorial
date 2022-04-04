"""Main tutorial app."""

import math

from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3


class MyApp(ShowBase):
    """Tutorial app."""

    def __init__(self) -> None:
        """Create a new app."""
        super().__init__()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        def spin_camera_task(task: Task) -> Task.cont:
            angle_deg = task.time * 6.0
            angle_rad = math.radians(angle_deg)
            self.camera.setPos(20 * math.sin(angle_rad), -20 * math.cos(angle_rad), 3)
            self.camera.setHpr(angle_deg, 0, 0)
            return Task.cont

        # Add the spinCameraTask procedure to the task manager.
        # self.taskMgr.add(spin_camera_task(self.camera), "SpinCameraTask")
        self.taskMgr.add(spin_camera_task, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pos_interval_1 = self.pandaActor.posInterval(
            13, Point3(0, -10, 0), startPos=Point3(0, 10, 0)
        )
        pos_interval_2 = self.pandaActor.posInterval(
            13, Point3(0, 10, 0), startPos=Point3(0, -10, 0)
        )
        hpr_interval_1 = self.pandaActor.hprInterval(
            3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0)
        )
        hpr_interval_2 = self.pandaActor.hprInterval(
            3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0)
        )
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(
            pos_interval_1,
            hpr_interval_1,
            pos_interval_2,
            hpr_interval_2,
            name="pandaPace",
        )
        self.pandaPace.loop()


# def spin_camera_task(camera):
#     def make_task(task):
#         angle_deg = task.time * 6.0
#         angle_rad = math.radians(angle_deg)
#         camera.setPos(20 * math.sin(angle_rad), -20 * math.cos(angle_rad), 3)
#         camera.setHpr(angle_deg, 0, 0)
#         return Task.cont
#
#     return make_task


def main() -> None:
    """Run the app."""
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
