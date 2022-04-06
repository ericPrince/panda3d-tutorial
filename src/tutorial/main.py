"""Main tutorial app."""

# import math
from pathlib import Path

from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AmbientLight,
    DirectionalLight,
    Vec4,
    WindowProperties,
    loadPrcFileData,
)

# from direct.interval.IntervalGlobal import Sequence
# from direct.task import Task
# from panda3d.core import Point3


class MyApp(ShowBase):
    """Tutorial app."""

    def __init__(self) -> None:
        """Create a new app."""
        super().__init__()
        self.disableMouse()

        self.actors = []

        win_props = WindowProperties()
        win_props.setSize(1000, 750)
        self.win.requestProperties(win_props)

        env_model = self.loader.loadModel("environment")
        env_model.reparentTo(self.render)

        panda_chan = Actor(
            "panda_chan/act_p3d_chan",
            {"walk": "panda_chan/a_p3d_chan_run"},
        )
        # actors must not go out of scope (even if in scene graph...)
        self.actors.append(panda_chan)
        panda_chan.reparentTo(self.render)
        # panda_chan.setPos(0, 7, 0)
        panda_chan.getChild(0).setH(180)
        panda_chan.loop("walk")

        self.camera.setPos(0, 0, 32)
        self.camera.setP(-90)

        ambient_light = AmbientLight("ambient light")
        ambient_light.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.render.setLight(self.render.attachNewNode(ambient_light))

        main_light = DirectionalLight("main light")
        main_light_node_path = self.render.attachNewNode(main_light)
        # Turn it around by 45 degrees, and tilt it down by 45 degrees
        main_light_node_path.setHpr(45, -45, 0)
        self.render.setLight(main_light_node_path)

        self.render.setShaderAuto()


def main() -> None:
    """Run the app."""
    loadPrcFileData(
        "", f"model-path {(Path(__file__).parents[2] / 'models').resolve()}"
    )
    app = MyApp()
    app.run()


if __name__ == "__main__":
    main()
