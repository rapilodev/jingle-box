#!/usr/bin/env perl
use strict;
use warnings;
use JSON;
use File::Basename;

print "Content-type: application/json; charset=utf-8\n\n";

sub tree {
    my $d = shift;
    warn $d;
    opendir my $dh, $d or return [];
    my (@dirs, @files);
    for my $e (sort grep { !/^\.\.?$/ } readdir $dh) {
        my $p = "$d/$e";
        if (-d $p) { push @dirs, $e; }
        elsif ($e =~ /\.(?:wav|mp3)$/) { push @files, $e; }
    }
    closedir $dh;

    if (@dirs && !@files) { return { map { $_ => tree("$d/$_") } @dirs }; }
    elsif (@files && !@dirs) { return \@files; }
    else { return { map { $_ => tree("$d/$_") } @dirs }; }
}

my $json = JSON->new->utf8(0)->canonical(1)->pretty(1);
my $data = tree(dirname(__FILE__)."/profile/");
print $json->encode($data);

