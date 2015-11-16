#!/usr/bin/env python

IPSO_OBJECTS = {
    0: {
        "required": (),
        "title": "LWM2M Security",
        "attrib": [
            {
                "attr_type": "str",
                "description": "LWM2M Server URI",
                "id": "0",
                "methods": "R",
                "range_value": "0-255",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Bootstrap Server",
                "id": "1",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Security Mode",
                "id": "2",
                "methods": "R",
                "range_value": "0-3",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Public Key or Identity",
                "id": "3",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Server Public Key or Identity",
                "id": "4",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Secret Key",
                "id": "5",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "SMS Security Mode",
                "id": "6",
                "methods": "R",
                "range_value": "0-255",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "SMS Binding Key Parameters",
                "id": "7",
                "methods": "E",
                "range_value": "6",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "SMS Binding Secret Keys",
                "id": "8",
                "methods": "E",
                "range_value": "32-48",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "LWM2M Server SMS Number",
                "id": "9",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Short Server ID",
                "id": "10",
                "methods": "R",
                "range_value": "1-65535",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Client Hold Off Time",
                "id": "11",
                "methods": "R",
                "range_value": "",
                "units": "s"
            }
        ]
    },
    1: {
        "required": (),
        "title": "LWM2M Server",
        "attrib": [
            {
                "attr_type": "int",
                "description": "Short Server ID",
                "id": "0",
                "methods": "R",
                "range_value": "1-65535",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Lifetime",
                "id": "1",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "int",
                "description": "Default Minimum Period",
                "id": "2",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "int",
                "description": "Default Maximum Period",
                "id": "3",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "",
                "description": "Disable",
                "id": "4",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Disable Timeout",
                "id": "5",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "bool",
                "description": "Notification Storing When Disabled or Offline",
                "id": "6",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Binding",
                "id": "7",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "",
                "description": "Registration Update Trigger",
                "id": "8",
                "methods": "E",
                "range_value": "",
                "units": ""
            }
        ]
    },
    2: {
        "required": (),
        "title": "LWM2M Access control",
        "attrib": [
            {
                "attr_type": "int",
                "description": "Object ID",
                "id": "0",
                "methods": "R",
                "range_value": "1-65535",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Object Instance ID",
                "id": "1",
                "methods": "R",
                "range_value": "0-65535",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "ACL",
                "id": "2",
                "methods": "RW",
                "range_value": "2",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Access Control Owner",
                "id": "3",
                "methods": "RW",
                "range_value": "0-65535",
                "units": ""
            }
        ]
    },
    3: {
        "required": (9, 10),
        "title": "Device",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Manufacturer",
                "id": "0",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Model Number",
                "id": "1",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Serial Number",
                "id": "2",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Firmware Version",
                "id": "3",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "",
                "description": "Reboot",
                "id": "4",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "",
                "description": "Factory Reset",
                "id": "5",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Available Power Sources",
                "id": "6",
                "methods": "R",
                "range_value": "0-7",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Power Source Voltage",
                "id": "7",
                "methods": "R",
                "range_value": "",
                "units": "mV"
            },
            {
                "attr_type": "int",
                "description": "Power Source Current",
                "id": "8",
                "methods": "R",
                "range_value": "",
                "units": "mA"
            },
            {
                "attr_type": "int",
                "description": "Battery Level",
                "id": "9",
                "methods": "R",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "Memory Free",
                "id": "10",
                "methods": "R",
                "range_value": "",
                "units": "KB"
            },
            {
                "attr_type": "int",
                "description": "Error Code",
                "id": "11",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "",
                "description": "Reset Error Code",
                "id": "12",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "time",
                "description": "Current Time",
                "id": "13",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "UTC Offset",
                "id": "14",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Timezone",
                "id": "15",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Supported Binding and Modes",
                "id": "16",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    4: {
        "required": (),
        "title": "Connectivity Monitoring",
        "attrib": [
            {
                "attr_type": "int",
                "description": "Network Bearer",
                "id": "0",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Available Network Bearer",
                "id": "1",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Radio Signal Strength",
                "id": "2",
                "methods": "R",
                "range_value": "",
                "units": "dBm"
            },
            {
                "attr_type": "int",
                "description": "Link Quality",
                "id": "3",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "IP Addresses",
                "id": "4",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Router IP Addresses",
                "id": "5",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Link Utilization",
                "id": "6",
                "methods": "R",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "str",
                "description": "APN",
                "id": "7",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Cell ID",
                "id": "8",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "SMNC",
                "id": "9",
                "methods": "R",
                "range_value": "",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "SMCC",
                "id": "10",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    5: {
        "required": (),
        "title": "Firmware Update",
        "attrib": [
            {
                "attr_type": "opaque",
                "description": "Package",
                "id": "0",
                "methods": "W",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Package URI",
                "id": "1",
                "methods": "W",
                "range_value": "0-255",
                "units": ""
            },
            {
                "attr_type": "",
                "description": "Update",
                "id": "2",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "State",
                "id": "3",
                "methods": "R",
                "range_value": "1-3",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Update Supported Objects",
                "id": "4",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Update Result",
                "id": "5",
                "methods": "R",
                "range_value": "0-6",
                "units": ""
            }
        ]
    },
    6: {
        "required": (0, 1),
        "title": "Location",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Latitude",
                "id": "0",
                "methods": "R",
                "range_value": "",
                "units": "Deg"
            },
            {
                "attr_type": "str",
                "description": "Longitude",
                "id": "1",
                "methods": "R",
                "range_value": "",
                "units": "Deg"
            },
            {
                "attr_type": "str",
                "description": "Altitude",
                "id": "2",
                "methods": "R",
                "range_value": "",
                "units": "m"
            },
            {
                "attr_type": "str",
                "description": "Uncertainty",
                "id": "3",
                "methods": "R",
                "range_value": "",
                "units": "m"
            },
            {
                "attr_type": "opaque",
                "description": "Velocity",
                "id": "4",
                "methods": "R",
                "range_value": "",
                "units": "Refers to 3GPP GAD specs"
            },
            {
                "attr_type": "time",
                "description": "Timestamp",
                "id": "5",
                "methods": "R",
                "range_value": "0-6",
                "units": ""
            }
        ]
    },
    7: {
        "required": (),
        "title": "Connectivity Statistics",
        "attrib": [
            {
                "attr_type": "int",
                "description": "SMS Tx Counter",
                "id": "0",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "SMS Rx Counter",
                "id": "1",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Tx Data",
                "id": "2",
                "methods": "R",
                "range_value": "",
                "units": "Kilo-Bytes"
            },
            {
                "attr_type": "int",
                "description": "Rx Data",
                "id": "3",
                "methods": "R",
                "range_value": "",
                "units": "Kilo-Bytes"
            },
            {
                "attr_type": "int",
                "description": "Max Message Size",
                "id": "4",
                "methods": "R",
                "range_value": "",
                "units": "Byte"
            },
            {
                "attr_type": "int",
                "description": "Average Message Size",
                "id": "5",
                "methods": "R",
                "range_value": "",
                "units": "Byte"
            },
            {
                "attr_type": "",
                "description": "StartOrReset",
                "id": "5",
                "methods": "E",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3200: {
        "required": (),
        "title": "Digital Input",
        "attrib": [
            {
                "attr_type": "bool",
                "description": "Digital Input State",
                "id": "5500",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Counter",
                "id": "5501",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Digital Input Polarity",
                "id": "5502",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Debounce Period",
                "id": "5503",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            },
            {
                "attr_type": "int",
                "description": "Digital Input Edge Selection",
                "id": "5504",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Digital Input Counter Reset",
                "id": "5505",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3201: {
        "required": (),
        "title": "Digital Output",
        "attrib": [
            {
                "attr_type": "bool",
                "description": "Digital Output State",
                "id": "5550",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "Digital Output Polarity",
                "id": "5551",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3202: {
        "required": (),
        "title": "Analogue Input",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Analog Input Current Value",
                "id": "5600",
                "methods": "R",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3203: {
        "required": (),
        "title": "Analogue Output",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Analog Output Current Value",
                "id": "5650",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3300: {
        "required": (),
        "title": "Generic Sensor",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3301: {
        "required": (),
        "title": "Illuminance Sensor",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3302: {
        "required": (),
        "title": "Presence Sensor",
        "attrib": [
            {
                "attr_type": "bool",
                "description": "Digital Input State",
                "id": "5500",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Digital Input Counter",
                "id": "5501",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Digital Input Counter Reset",
                "id": "5505",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Type",
                "id": "5751",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Busy to Clear delay",
                "id": "5903",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            },
            {
                "attr_type": "int",
                "description": "Clear to Busy delay",
                "id": "5904",
                "methods": "RW",
                "range_value": "",
                "units": "ms"
            }
        ]
    },
    3303: {
        "required": (5700,),
        "title": "Temperature Sensor",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3304: {
        "required": (5700,),
        "title": "Humidity Sensor",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3305: {
        "required": (),
        "title": "Power Measurement",
        "attrib": [
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Instantaneous active power",
                "id": "5800",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Min Measured active power",
                "id": "5801",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Max Measured active power",
                "id": "5802",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Min Range active power",
                "id": "5803",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Max Range active power",
                "id": "5804",
                "methods": "R",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Active Power Calibration",
                "id": "5806",
                "methods": "W",
                "range_value": "",
                "units": "W"
            },
            {
                "attr_type": "float",
                "description": "Instantaneous reactive power",
                "id": "5810",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Min Measured reactive power",
                "id": "5811",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Max Measured reactive power",
                "id": "5812",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range reactive power",
                "id": "5813",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Max Range reactive power",
                "id": "5814",
                "methods": "R",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Cumulative reactive power",
                "id": "5815",
                "methods": "R",
                "range_value": "",
                "units": "varh"
            },
            {
                "attr_type": "float",
                "description": "Reactive Power Calibration",
                "id": "5816",
                "methods": "W",
                "range_value": "",
                "units": "var"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Current Calibration",
                "id": "5821",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Cumulative energy",
                "id": "5822",
                "methods": "E",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3306: {
        "required": (),
        "title": "Actuation",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            },
            {
                "attr_type": "str",
                "description": "Multi-state Output",
                "id": "5853",
                "methods": "RW",
                "range_value": "",
                "units": ""
            }
        ]
    },
    3308: {
        "required": (),
        "title": "Set Point",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Colour",
                "id": "5706",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Application Type",
                "id": "5750",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "SetPoint Value",
                "id": "5900",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            }
        ]
    },
    3310: {
        "required": (),
        "title": "Load Control",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Event Identifier",
                "id": "5823",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "time",
                "description": "Start Time",
                "id": "5824",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Duration In Min",
                "id": "5825",
                "methods": "RW",
                "range_value": "",
                "units": "min"
            },
            {
                "attr_type": "int",
                "description": "Criticality Level",
                "id": "5826",
                "methods": "RW",
                "range_value": "0-3",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Avg Load AdjPct",
                "id": "5827",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "Duty Cycle",
                "id": "5828",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            }
        ]
    },
    3311: {
        "required": (),
        "title": "Light Control",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Colour",
                "id": "5706",
                "methods": "RW",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            }
        ]
    },
    3312: {
        "required": (),
        "title": "Power Control",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Cumulative active power",
                "id": "5805",
                "methods": "R",
                "range_value": "",
                "units": "Wh"
            },
            {
                "attr_type": "float",
                "description": "Power factor",
                "id": "5820",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "bool",
                "description": "On/Off",
                "id": "5850",
                "methods": "RW",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "int",
                "description": "Dimmer",
                "id": "5851",
                "methods": "RW",
                "range_value": "0-100",
                "units": "%"
            },
            {
                "attr_type": "int",
                "description": "On time",
                "id": "5852",
                "methods": "RW",
                "range_value": "",
                "units": "s"
            }
        ]
    },
    3313: {
        "required": (),
        "title": "Accelometer",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "X Value",
                "id": "5702",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Y Value",
                "id": "5703",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Z Value",
                "id": "5704",
                "methods": "R",
                "range_value": "",
                "units": "units"
            }
        ]
    },
    3314: {
        "required": (),
        "title": "Magnetometer",
        "attrib": [
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "X Value",
                "id": "5702",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Y Value",
                "id": "5703",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Z Value",
                "id": "5704",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "float",
                "description": "Compass Direction",
                "id": "5705",
                "methods": "R",
                "range_value": "360",
                "units": "deg"
            }
        ]
    },
    3315: {
        "required": (),
        "title": "Barometer",
        "attrib": [
            {
                "attr_type": "float",
                "description": "Min Measured Value",
                "id": "5601",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Measured Value",
                "id": "5602",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Min Range Value",
                "id": "5603",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Max Range Value",
                "id": "5604",
                "methods": "R",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "opaque",
                "description": "Reset Min and Max Measured Values",
                "id": "5605",
                "methods": "E",
                "range_value": "",
                "units": ""
            },
            {
                "attr_type": "float",
                "description": "Sensor Value",
                "id": "5700",
                "methods": "R",
                "range_value": "",
                "units": "units"
            },
            {
                "attr_type": "str",
                "description": "Sensor Units",
                "id": "5701",
                "methods": "R",
                "range_value": "",
                "units": ""
            }
        ]
    }
}

