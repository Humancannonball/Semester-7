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
