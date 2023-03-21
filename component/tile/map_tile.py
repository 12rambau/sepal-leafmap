"""The map displayed in the map application."""

import ipyvuetify as v
from ipyleaflet import FullScreenControl, WidgetControl, basemaps
from leafmap.leafmap import Map
from sepal_ui import mapping as sm
from sepal_ui import sepalwidgets as sw


class MapTile(sw.Tile):
    def __init__(self):
        """Specific Map integrating all the widget components.

        Use this map to gather all your widget and place them on it. It will reduce the amount of work to perform in the notebook
        """
        # create a map
        default_basemap = (
            basemaps.CartoDB.DarkMatter
            if v.theme.dark is True
            else basemaps.CartoDB.Positron
        )
        self.m = Map(basemap=default_basemap, zoom=3)
        self.m._id = "geemap"
        self.m.add_class(self.m._id)

        # don't add the control to the map simply set it to fullscreen
        sm.FullScreenControl(self.m, fullscreen=True, fullapp=True)
        self.m.remove_control(
            next(c for c in self.m.controls if isinstance(c, FullScreenControl))
        )

        # create the tile
        super().__init__("map_tile", "", [self.m])

    def set_code(self, link):
        """Add the code link btn to the map."""
        btn = sm.MapBtn("fa-solid fa-code", href=link, target="_blank")
        control = WidgetControl(widget=btn, position="bottomleft")
        self.m.add(control)

        return

    def set_wiki(self, link):
        """Add the wiki link btn to the map."""
        btn = sm.MapBtn("fa-solid fa-book-open", href=link, target="_blank")
        control = WidgetControl(widget=btn, position="bottomleft")
        self.m.add(control)

        return

    def set_issue(self, link):
        """Add the code link btn to the map."""
        btn = sm.MapBtn("fa-solid fa-bug", href=link, target="_blank")
        control = WidgetControl(widget=btn, position="bottomleft")
        self.m.add(control)

        return
