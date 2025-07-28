inverter_ip = "192.168.1.18"
inverter_port = 502
# Slave Defaults
# Sungrow: 0x01
# SMA: 3
slaves = [170,171]
model = "schneider-mppt80-600"
timeout = 3
scan_interval = 10
# Optional:
#dweepy_uuid = "random-uuid"
# Optional:
influxdb_ip = "192.168.1.5"
influxdb_port = 8086
influxdb_user = ""
influxdb_password = ""
influxdb_database = "schneider"
influxdb_ssl = False
influxdb_verify_ssl = False
# Optional
#mqtt_server = "192.168.1.128"
#mqtt_port = 1883
#mqtt_topic = "inverter/stats"

