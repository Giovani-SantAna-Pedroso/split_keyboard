import board
import digitalio
from kmk.bootcfg import bootcfg

# REAL key: Row0 + Col0
col = digitalio.DigitalInOut(board.GP15)  # C0
row = digitalio.DigitalInOut(board.GP19)  # R0
col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

holding_boot_key = row.value

row.deinit()
col.deinit()

if not holding_boot_key:
    # normal mode (fast boot for BIOS)
    bootcfg(
        storage=False,
        cdc_console=False,
        cdc_data=False,
        nkro=True,          # <-- this is the line that actually gets you NKRO
    )
else:
    # holding Q/ESC → enable USB drive + serial for dev/debug
    bootcfg(
        storage=True,
        cdc_console=True,
        cdc_data=True,
        nkro=True,
    )



# old 
# import supervisor
# import board
# import digitalio
# import storage
# import usb_cdc
# import usb_hid
#
# supervisor.set_next_stack_limit(8192)
#
# # REAL key: Row0 + Col0
# col = digitalio.DigitalInOut(board.GP15)  # C0
# row = digitalio.DigitalInOut(board.GP19)  # R0
#
# col.switch_to_output(value=True)
# row.switch_to_input(pull=digitalio.Pull.DOWN)
#
# if not row.value:
#     # normal mode (fast boot for BIOS)
#     storage.disable_usb_drive()
#     usb_cdc.disable()
#     usb_hid.enable(boot_device=1)
# else:
#     # holding Q/ESC → enable USB
#     storage.enable_usb_drive()
#     usb_cdc.enable(console=True, data=True)
#
# row.deinit()
# col.deinit()
