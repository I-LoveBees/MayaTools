import maya.cmds as cmds
import re  # Import regex module to validate attribute names


def setup_follow_driven_keys_from_selection(follow_attr):
    """
    Automates the setup of driven keys for a follow system using an enum attribute,
    ensuring weight attributes end with a number after 'W'.

    :param follow_attr: The name of the follow enum attribute on the driver object (e.g., 'Follow').
    """
    # Get the current selection
    selection = cmds.ls(selection=True)
    if len(selection) < 3:
        cmds.error("Please select the driver object first, followed by the two driven constraints.")
        return

    driver = selection[0]  # The first selected object is the driver
    driven_constraints = selection[1:]  # Remaining selections are the driven constraints

    # Check if the driver has the follow attribute
    if not cmds.attributeQuery(follow_attr, node=driver, exists=True):
        cmds.error(f"The attribute '{follow_attr}' does not exist on the driver object '{driver}'.")
        return

    # Get the enum values from the Follow attribute
    enum_values = cmds.attributeQuery(follow_attr, node=driver, listEnum=True)[0].split(':')
    num_enum_values = len(enum_values)
    print(f"Enum values detected: {enum_values} ({num_enum_values} total)")

    # Prepare to collect weight attributes for each driven constraint
    all_weight_attrs = []

    for constraint in driven_constraints:
        # Detect weight attributes ending with 'W' followed by a number
        weight_attrs = cmds.listAttr(constraint, string="*W*") or []
        valid_weight_attrs = [
            f"{constraint}.{attr}" for attr in weight_attrs
            if re.match(r".*W\d+$", attr) and cmds.objExists(f"{constraint}.{attr}")
        ]

        # Ensure the detected attributes match the number of enum values
        if len(valid_weight_attrs) != num_enum_values:
            print(f"Constraint '{constraint}' detected weight attributes: {valid_weight_attrs}")
            cmds.error(f"Constraint '{constraint}' is missing or has mismatched weight attributes.")
            return

        print(f"Constraint '{constraint}' weights detected: {valid_weight_attrs}")
        all_weight_attrs.append(valid_weight_attrs)

    # Iterate through each enum value and set driven keys
    for i in range(num_enum_values):
        # Set the driver attribute to the current enum index
        cmds.setAttr(f"{driver}.{follow_attr}", i)

        # Update weights for all driven constraints
        for weight_attrs in all_weight_attrs:
            for j, weight_attr in enumerate(weight_attrs):
                weight = 1 if i == j else 0  # Set 1 for the active constraint, 0 for others
                cmds.setAttr(weight_attr, weight)
                cmds.setDrivenKeyframe(weight_attr, currentDriver=f"{driver}.{follow_attr}")

    print(f"Driven keys successfully set up for {follow_attr} on {driver}.")


# Example usage:
# Select the driver object first, then the two driven constraints, and run the script.
setup_follow_driven_keys_from_selection("Follow")