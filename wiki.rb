#!/usr/bin/env ruby

=begin
get info of items from wikipedia

python wiki.rb -i [any item]

require wikipedia, thor
=end

require 'wikipedia'

require "thor"
 
class WikiCLI < Thor
    # ruby wiki.rb find --item Python
    desc "Wiki", "Ruby cli for Wikipedia"
    option :item, :aliases => :i
    option :part, :aliases => :p, :default => 'summary'
    def find
        page = Wikipedia.find(n=options[:item])
        puts page.send(options[:part])
    end
end
 
WikiCLI.start(ARGV)