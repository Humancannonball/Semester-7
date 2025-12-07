local cjson = require "cjson"

local function read_file(path)
    local file, err = io.open(path, "r")
    if not file then return nil, err end
    local content = file:read("*a")
    file:close()
    return content
end

local function increment_mac(mac)
    -- Increment the last byte of the MAC address
    local prefix = mac:sub(1, 15)
    local last_byte = tonumber(mac:sub(16, 17), 16)
    last_byte = (last_byte + 1) % 256
    return string.format("%s%02X", prefix, last_byte)
end

local function main()
    local content, err = read_file("data.json")
    if not content then
        print("Error reading file: " .. err)
        return
    end

    local data = cjson.decode(content)

    print("Processing Ports and Modifying MAC Addresses:")
    print("---------------------------------------------")

    for k, v in pairs(data.ports) do
        local old_mac = v.mac
        v.mac = increment_mac(old_mac)
        print(string.format("Port: %s | Old MAC: %s | New MAC: %s", v.name, old_mac, v.mac))
    end
    print("---------------------------------------------")
    
    -- In a real scenario, we might write this back to a file
    -- local new_json = cjson.encode(data)
    -- print("\nNew JSON Structure:")
    -- print(new_json)
end

main()
