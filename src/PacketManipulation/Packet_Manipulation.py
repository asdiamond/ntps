#!/usr/bin/env python3

from scapy.all import *

#Functions to interact with packets using scapy

def sendPackets(pkt):
	send(pkt)

def readFromPCAP(filename):
	packets = rdpcap("filename")

#Sniff can be used as a capture filter if enough attributes are provided
#Example: pkts = sniff(count = 100, filter = "icmp and ip host 4.2.2.1")
def capturePackets():
	packets = sniff()
	
def capturePackets(limit):
	packets = sniff(count = limit)
	
def displayPackets():
	_.summary()

def displayPackets(packets):
	packets.summary()

def viewPacketInfo():
	_.show()
	
def viewPacketInfo(pkt):
	pkt.show()

#To disassemble the packet and get a specific protocol layer, use the [] operator: _[IP]
def viewProtocol(protocol):
	_[protocol]
	
#to view layers of a packet use ls()
def viewLayers():
	_.ls()
	
def viewLayers(pkt):
	pkt.ls()
#to view the fields in a layer use ls(IPv6), can use
#arp, ip, ipv6, tcp, udp, icmp

def viewLayerFields(pkt, layer):
	pkt.ls(layer)

def checkLayer(layer):
	return _.haslayer(layer)

#Packet layer fields are python variables and can be modified as such
#to edit specific fields in a given layer, packet[IP].dst = "1.2.3.4"

def modifyLayerDst(layer, dest):
	_[layer].dst = dest

def modifyLayerDst(pkt, layer, dest):
	pkt[layer].dst = dest

def modifyLayerSrc(layer, source):
	_[layer].src = source

def modifyLayerSrc(pkt, layer, source):
	pkt[layer].src = source
	
def modifyLayerType(layer, tp):
	_[layer].type = tp

#to view a packet source port use, packet.sport
#to modify the source port, packet.sport = 443

def modifySourcePort(port):
	_.sport = port
	
def modifySourcePort(pkt, port):
	pkt.sport = port



