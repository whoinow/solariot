schneider_registers = [
  ['58 - Output DC Voltage',0x0058,'S32', 'FIX3'],
  ['5A - Output DC Current',0x005A,'S32','FIX3'],
  ['5C - Output DC Power',0x005C,'U32','RAW'],
  ['4C - Input DC Voltage',0x004C, 'U32', 'FIX3'],
  ['4E - Input DC Current',0x004E, 'U32', 'FIX3'],
  ['50 - Input DC Power',0x0050, 'U32', 'RAW'],
  ['70 - Energy From PV This Hour (kWh)', 0x0070, 'U32', 'FIX3'],
  ['74 - Energy From PV Today (kWh)', 0x0074, 'U32', 'FIX3'],
  ['8C - Energy to Battery Today (kWh)', 0x008C, 'U32', 'FIX3']
]

# scan is not used for Schneider inverters but solariot.py expects it to exist
scan = "{}"