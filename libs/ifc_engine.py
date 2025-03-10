"""

"""
import os
import ifcopenshell
from ifcopenshell import entity_instance, file as ifc_file


class IfcEngine:

    def __init__(self, ifc_filename: str):
        assert os.path.exists(ifc_filename), f"[>_<] File not found: {ifc_filename}"
        self.ifc = ifcopenshell.open(ifc_filename, should_stream=True)


def main():
    pass


if __name__ == '__main__':
    main()
