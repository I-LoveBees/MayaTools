import maya.cmds as cmds


class PlacementGenUI():
    ui_name = 'PlacementGenerator'
    window_name = '%sWindow' % ui_name

    def __init__(self):
        self.y_col = None
        self.x_col = None
        self.z_col = None
        self.dup_num = None
        self.btn_cmd_gen = None
        self.dups = None
        self.z_max = None
        self.z_min = None
        self.y_max = None
        self.y_min = None
        self.x_min = None
        self.x_max = None
        self.m_col = None

    def delete(self):
        # check to see if exists, delete if true
        if cmds.window(PlacementGenUI.window_name, exists=True):
            cmds.deleteUI(PlacementGenUI.window_name)

    def create(self):
        self.delete()
        # create window, assigned 'window' to the name 'calculate' and reassigned it to PlacementGenUI.window_name
        self.window_name = cmds.window(PlacementGenUI.window_name,
                                       title='%s Tool' % PlacementGenUI.window_name)

        # define layout
        self.m_col = cmds.columnLayout(parent=PlacementGenUI.window_name, adj=True, nch=8)
        self.x_col = cmds.columnLayout(p=self.m_col, adj=True, numberOfChildren=4)
        self.x_min = cmds.floatSliderGrp(p=self.x_col, adj=True, field=True, label='X Min:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        self.x_max = cmds.floatSliderGrp(p=self.x_col, adj=True, field=True, label='X Max:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        cmds.separator(p=self.m_col, h=20, style='in')
        self.y_col = cmds.columnLayout(p=self.m_col, adj=True, numberOfChildren=4)
        self.y_min = cmds.floatSliderGrp(p=self.y_col, adj=True, field=True, label='Y Min:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        self.y_max = cmds.floatSliderGrp(p=self.y_col, adj=True, field=True, label='Y Max:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        cmds.separator(p=self.m_col, h=20, style='in')
        self.z_col = cmds.columnLayout(p=self.m_col, adj=True, numberOfChildren=4)
        self.z_min = cmds.floatSliderGrp(p=self.z_col, adj=True, field=True, label='Z Min:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        self.z_max = cmds.floatSliderGrp(p=self.z_col, adj=True, field=True, label='Z Max:',
                                         minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0)
        cmds.separator(p=self.m_col, h=20, style='in')
        self.dups = cmds.columnLayout(p=self.m_col, adj=True, numberOfChildren=3)
        self.dup_num = cmds.intSliderGrp(p=self.dups, adj=True, field=True, label='Number of Duplicates:',
                                         minValue=1, maxValue=20, fieldMinValue=1, fieldMaxValue=100, value=1)
        cmds.separator(p=self.m_col, h=20, style='in')
        self.btn_cmd_gen = cmds.button(p=self.m_col, label='Generate Objects', c=lambda a: self.btn_gen())

        self.show()

    def show(self):
        # create window itself
        cmds.showWindow(PlacementGenUI.window_name)

    def btn_gen(self):
        import placementGenerator
        # get ranges from selection
        xmin = cmds.floatSliderGrp(self.x_min, q=True, v=True)
        xmax = cmds.floatSliderGrp(self.x_max, q=True, v=True)
        ymin = cmds.floatSliderGrp(self.y_min, q=True, v=True)
        ymax = cmds.floatSliderGrp(self.y_max, q=True, v=True)
        zmin = cmds.floatSliderGrp(self.z_min, q=True, v=True)
        zmax = cmds.floatSliderGrp(self.z_max, q=True, v=True)
        numdups = cmds.intSliderGrp(self.dup_num, q=True, v=True)

        # apply ranges to place gen code
        placementGenerator.placementGenerator(xmin, xmax, ymin, ymax, zmin, zmax, numdups)

