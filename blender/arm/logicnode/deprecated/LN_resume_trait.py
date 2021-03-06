from arm.logicnode.arm_nodes import *


@deprecated('Set Trait Paused')
class ResumeTraitNode(ArmLogicTreeNode):
    """Resumes the given trait."""
    bl_idname = 'LNResumeTraitNode'
    bl_label = 'Resume Trait'
    bl_description = "Please use the \"Set Trait Paused\" node instead"
    arm_category = 'Trait'
    arm_version = 2

    def init(self, context):
        super(ResumeTraitNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Trait')
        self.add_output('ArmNodeSocketAction', 'Out')
