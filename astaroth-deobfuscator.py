import idautils
import idc
import ida_bytes

start = 0
end = 0

for function in idautils.Functions():
    #Loop on each instruction of the function
    for x in idautils.FuncItems(function):
        #Find the call to the junk function
        if idc.print_insn_mnem(x) == 'call' and idc.print_operand(x, 0) == 'time_waster_3000':
            #Go backwards to the push of the first argument
            start = x - 35
            #Go forwards to include the call instruction (5 bytes long) to the hidden block
            end = x + 5
            #Hide it
            ida_bytes.del_hidden_range(start)
            ida_bytes.add_hidden_range(start,end,'','','',0xFFFFFF)
