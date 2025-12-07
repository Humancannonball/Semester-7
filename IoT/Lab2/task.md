Lua regex and data parsing handling
Task 1
Write small application that would access json type file, and if it matches radio protocol as
“11ad”, which is located under radios.wlan0 data, would print-out currently used channel,
frequency, and channelWidth elements
{
"radios": {
"wlan0": {
"mac": "C4:93:00:32:DF:9D",
"name": "wlan0",
"phy": "phy0",
"protocol": "11ad",
"antennas": 0,
"txPower": 0,
"channel": 6,
"frequency": 69120,
"channelWidth": 2160,
"noise": 0,
"countryCode": "00",
"vendor": "prs",
"T_radio": 6000,
"T_mac": 25000
}
},
"vaps": [
{
"ifIndex": 14,
"name": "wlan0",
"mac": "C4:93:00:32:DF:9D",
"radio": "wlan0",
"operationMode": "master",
"ssid": "179",
"hiddenSsid": false,
"peerCount": 1,
"security": "WPA2-PSK (AES)",
"maxPeerCount": 32,
"rxmcs": 4,
"rxPackets": 13145561497,
"rxErrors": 0,
}
]
}
Task #2
Write a small application that would read firmware version string. And print-out only if the
firmware string matches the “6.8.6296952” line. Use the provided string line below.
Falcon UMAC 6.8.6296952 Linux
May 2 2023 09:31:59 sw_build
Prepare code output for report