# Lab 2: Lua Regex and Data Parsing

## Objective
Two tasks involving JSON parsing and pattern matching in Lua.

---

## Task 1: Radio Protocol Parsing

### Description
Read a JSON file and if the radio protocol under `radios.wlan0` matches "11ad", print the channel, frequency, and channelWidth.

### radio_data.json
```json
{
    "radios": {
        "wlan0": {
            "mac": "C4:93:00:32:DF:9D",
            "protocol": "11ad",
            "channel": 6,
            "frequency": 69120,
            "channelWidth": 2160
        }
    }
}
```

### task1.lua
```lua
local cjson = require "cjson"

local function read_file(path)
    local file, err = io.open(path, "r")
    if not file then return nil, err end
    local content = file:read("*a")
    file:close()
    return content
end

local function main()
    local content, err = read_file("radio_data.json")
    if not content then
        print("Error reading file: " .. err)
        return
    end

    local data = cjson.decode(content)
    local wlan0 = data.radios.wlan0

    if wlan0 and wlan0.protocol == "11ad" then
        print("Protocol matches '11ad'!")
        print("Channel: " .. wlan0.channel)
        print("Frequency: " .. wlan0.frequency)
        print("Channel Width: " .. wlan0.channelWidth)
    else
        print("Protocol does not match '11ad'")
    end
end

main()
```

### Output
```
Protocol matches '11ad'!
Channel: 6
Frequency: 69120
Channel Width: 2160
```

---

## Task 2: Firmware Version Regex Matching

### Description
Parse a firmware version string and print only if it matches "6.8.6296952".

### task2.lua
```lua
local firmware_string = "Falcon UMAC 6.8.6296952 Linux May 2 2023 09:31:59 sw_build"
local target_version = "6.8.6296952"

-- Extract version using pattern matching
local version = firmware_string:match("(%d+%.%d+%.%d+)")

if version == target_version then
    print("Firmware version matches: " .. version)
else
    print("Firmware version does not match. Found: " .. (version or "none"))
end
```

### Output
```
Firmware version matches: 6.8.6296952
```

---

## Conclusion
- Task 1 demonstrates JSON parsing with cjson and conditional logic to check protocol type
- Task 2 shows Lua pattern matching using `%d+%.%d+%.%d+` to extract version strings
