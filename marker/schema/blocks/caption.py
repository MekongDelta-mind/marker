from marker.schema import BlockTypes
from marker.schema.blocks import Block


class Caption(Block):
    block_type: BlockTypes = BlockTypes.Caption
    block_description: str = "A text caption that is directly above or below an image or table. Only used for text describing the image or table.  "

    def assemble_html(self, document, child_blocks, parent_structure):
        template = super().assemble_html(document, child_blocks, parent_structure)
        template = template.replace("\n", " ")
        return f"<p>{template}</p>"
