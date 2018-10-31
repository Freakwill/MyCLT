#!/usr/local/bin/lua

local argparse = require "argparse"

local parser = argparse("head", "Read the first n lines of a file")
parser:option("-f --filename", "File name")
parser:option("-n --lines", "The number of lines", 1)

local args = parser:parse()

file = io.open(args["filename"])
n = args["lines"]

s = file:lines()
for k = 1, n do
    print(s(k))
end

file:close()

