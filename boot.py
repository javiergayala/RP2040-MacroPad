import storage
import usb_cdc

# Disable the CIRCUITPY USB Drive
# To re-enable the CIRCUITPY driver
# boot into SAFE MODE
storage.disable_usb_drive()
usb_cdc.enable(console=False, data=True)
