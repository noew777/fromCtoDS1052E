#!/usr/bin/env python3
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources()) # Prints "()" => No instruments found!