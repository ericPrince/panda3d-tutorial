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
        scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        scene.setScale(0.25, 0.25, 0.25)
        scene.setPos(-8, 42, 0)

        def spin_camera_task(task: Task) -> Task.cont:
            angle_deg = task.time * 6.0
            angle_rad = math.radians(angle_deg)
            self.camera.setPos(20 * math.sin(angle_rad), -20 * math.cos(angle_rad), 3)
            self.camera.setHpr(angle_deg, 0, 0)
            return Task.cont

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(spin_camera_task, "SpinCameraTask")

        # Load and transform the panda actor.
        panda_actor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        panda_actor.setScale(0.005, 0.005, 0.005)
        panda_actor.reparentTo(self.render)
        # Loop its animation.
        panda_actor.loop("walk")

        Sequence(
            panda_actor.posInterval(13, Point3(0, -10, 0), startPos=Point3(0, 10, 0)),
            panda_actor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0)),
            panda_actor.posInterval(13, Point3(0, 10, 0), startPos=Point3(0, -10, 0)),
            panda_actor.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0)),
            name="pandaPace",
        ).loop()


def main() -> None:
    """Run the app."""
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
