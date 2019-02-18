#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

=begin 
create a file
example:
python Scripts/new.py -f hello/readme.md  # even folder hello not exists
=end

require 'Thor'

$heads = {'py':'#!/usr/bin/env python3', 'rb':'#!/usr/bin/env ruby'}

class NewCLI < Thor
    # ruby new.rb new --item Python
    desc "New File", "Ruby cli for creating files"
    option :path, :aliases => :p, :default => 'test.txt'
    option :string, :aliases => :s, :default => ''
    option :file, :aliases => :f, :default => ''

    def new     
        if options[:string]
            content = options[:string]
        elsif options[:file]
            file = File.new(options[:file], "r")
            File.open("filename", "mode") do |file|
               content = file.sysread()
            end
        end

        File.open(options[:path], "w") do |file|
            suffix = options[:path].split('.')[-1]
            if $heads[suffix.to_sym]
                content = $heads[suffix.to_sym] + '/n/n' + content
            end
            file.syswrite(content)
        end
    end
end
 
NewCLI.start(ARGV)
