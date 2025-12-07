Basic Lua handing
Task: write a simple Lua based script, using Lua language, to create a basic handler, that would
change ethernet mac addresses in provided JSON type file:
On Linux/Windows PC install lua using apt install lua5.1 or apt install lua5.2
{
"ports": {
"eth0": {
"mac": "6C:10:8B:00:45:00",
"name": "eth0",
"link": false,
"autoneg": false
},
"eth1": {
"mac": "6C:10:8B:00:44:01",
"name": "eth1",
"link": false,
"autoneg": true
},
"eth2": {
"mac": "6C:10:8B:00:46:02",
"name": "eth2",
"link": false,
"autoneg": truea
},
"eth3": {
"mac": "6C:10:8B:00:47:03",
"name": "eth3",
"link": false,
"autoneg": true
},
"eth4": {
"mac": "6C:10:8B:00:48:04",
"name": "eth4",
"link": false,
"autoneg": true
},
"eth5": {
"mac": "6C:10:8B:00:49:05",
"name": "eth5",
}
}
}
"link": true,
"speed": 1000,
"duplex": "full",
"autoneg": true
Provide an example code as output for lab work