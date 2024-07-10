import maya.cmds as cmds


class MeshColorUI():
    ui_name = 'MeshColor'
    window_name = '%sWindow' % ui_name

    def __init__(self):
        self.btn_cmd_ok = None
        self.color = None
        self.m_col = None

    def delete(self):
        # check to see if exists, delete if true
        if cmds.window(MeshColorUI.window_name, exists=True):
            cmds.deleteUI(MeshColorUI.window_name)

    def create(self):
        self.delete()
        # create window, assigned 'window' to the name 'calculate' and reassigned it to MeshColorUI.window_name
        self.window_name = cmds.window(MeshColorUI.window_name,
                                       title='%s Tool' % MeshColorUI.window_name)

        # define layout
        self.m_col = cmds.columnLayout(p=MeshColorUI.window_name, adj=True)
        self.color = cmds.colorIndexSliderGrp(p=self.m_col, adj=True, label='Color Index', minValue=0, maxValue=32)
        self.btn_cmd_ok = cmds.button(p=self.m_col, label='Ok', command=lambda a: self.btn_ok())

        # show window
        self.show()

    def show(self):
        cmds.showWindow(MeshColorUI.window_name)

    def btn_ok(self):
        import meshColorChange
        # get color index info from ui
        color = cmds.colorIndexSliderGrp(self.color, q=True, v=True)
        # grab color change code and apply selected color
        meshColorChange.changeColor(color)

