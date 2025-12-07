local firmware_string = "Falcon UMAC 6.8.6296952 Linux May 2 2023 09:31:59 sw_build"
local target_version = "6.8.6296952"

-- Extract version using pattern matching
local version = firmware_string:match("(%d+%.%d+%.%d+)")

if version == target_version then
    print("Firmware version matches: " .. version)
else
    print("Firmware version does not match. Found: " .. (version or "none"))
end
