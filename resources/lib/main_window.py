
import threading
import os

import xbmc
import xbmcaddon
import xbmcgui

from .simple_logging import SimpleLogging
log = SimpleLogging(__name__)


class MainAppWindowThread(threading.Thread):

    keep_running = True

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        log.debug("MainAppWindowThread Running")

        __addon__ = xbmcaddon.Addon()
        __cwd__ = __addon__.getAddonInfo('path')
        PLUGINPATH = xbmc.translatePath(os.path.join(__cwd__))

        #xbmc.executebuiltin('Dialog.Close(busydialog)')
        main_window = MainAppWindow("MainAppWindow.xml", PLUGINPATH, "default", "720p")
        main_window.doModal()
        del main_window


class MainAppWindow(xbmcgui.WindowXML):#Dialog):

    main_list = None
    control_groups = {}

    def __init__(self, *args, **kwargs):
        log.debug("MainAppWindow: __init__")
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        log.debug("MainAppWindow: onInit")
        self.action_exitkeys_id = [10, 13]

        action_items = []

        li = xbmcgui.ListItem("Group 01")
        li.setProperty('group_id', 'group01')
        action_items.append(li)

        li = xbmcgui.ListItem("Group 02")
        li.setProperty('group_id', 'group02')
        action_items.append(li)

        self.main_list = self.getControl(3000)
        self.main_list.addItems(action_items)
        self.setFocus(self.main_list)

        list = xbmcgui.ControlList(360, 150, 300, 400)
        self.addControl(list)
        list.addItem('Item 1')
        list.addItem('Item 2')
        list.addItem('Item 3')
        list.setVisible(False)

        control_group = []
        control_group.append(list)
        self.control_groups["group01"] = control_group

        list2 = xbmcgui.ControlList(360, 150, 300, 400)
        self.addControl(list2)
        list2.addItem('Item 4')
        list2.addItem('Item 5')
        list2.addItem('Item 6')
        list2.setVisible(False)

        control_group = []
        control_group.append(list2)
        self.control_groups["group02"] = control_group

        '''
        for key in self.control_groups:
            log.debug("adding controls for group : {0}", key)
            controls = self.control_groups[key]
            log.debug("adding controls count : {0}", len(controls))
            for control in controls:
                log.debug("adding control {0}", control)
                #self.addControl(control)
                #control.setVisible(True)
        '''


    def onFocus(self, controlId):
        log.debug("MainAppWindow: onFocus")

    def doAction(self, actionID):
        log.debug("MainAppWindow: doAction")

    def onMessage(self, message):
        log.debug("ActionMenu: onMessage: {0}", message)

    def onAction(self, action):
        log.debug("ActionMenu: onAction: {0}", action.getId())

        if action.getId() in [3, 4]:
            selected_item = self.main_list.getSelectedItem()
            group_id = selected_item.getProperty("group_id")

            for key in self.control_groups:
                controls = self.control_groups[key]
                for control in controls:
                    control.setVisible(False)

            if group_id:
                controls = self.control_groups[group_id]
                log.debug("adding controls count : {0}", len(controls))
                for control in controls:
                    log.debug("adding control {0}", control)
                    control.setVisible(True)

        if action.getId() == 10:  # ACTION_PREVIOUS_MENU
            self.close()
        elif action.getId() == 92:  # ACTION_NAV_BACK
            self.close()

    def onClick(self, controlID):
        log.debug("ActionMenu: Selected Item: {0}", controlID)

        if controlID == 3000:

            selected_item = self.main_list.getSelectedItem()
            group_id = selected_item.getProperty("group_id")

            for key in self.control_groups:
                controls = self.control_groups[key]
                for control in controls:
                    control.setVisible(False)

            if group_id:
                controls = self.control_groups[group_id]
                log.debug("adding controls count : {0}", len(controls))
                for control in controls:
                    log.debug("adding control {0}", control)
                    control.setVisible(True)


