from marker.schema import BlockTypes
from marker.schema.blocks import Block


class Handwriting(Block):
    block_type: BlockTypes = BlockTypes.Handwriting
    block_description: str = "A region that contains handwriting."

    def assemble_html(self, document, child_blocks, parent_structure):
        template = super().assemble_html(document, child_blocks, parent_structure)
        template = template.replace("\n", " ")
        return f"<p>{template}</p>"
