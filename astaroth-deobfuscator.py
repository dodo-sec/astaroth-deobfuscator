import ida_bytes
import idautils
import idc

start = 0
end = 0
time_waster_slide = False

#Remember to replace 'sub_CHANGEME' with the name of your function

for function in idautils.Functions():
    #Loop on each instruction of the function
    for x in idautils.FuncItems(function):
        #Find the useless padding function
        if idc.print_insn_mnem(x) == 'call' and idc.print_operand(x, 0) == 'sub_CHANGEME':
            #Mark start address
            start = x - 35
            time_waster_slide = True
            #Loop until finding the end of a block of calls to padding function
            while time_waster_slide:
                if idc.print_insn_mnem(x + 40) != 'call' and idc.print_operand(x + 40, 0) != 'sub_CHANGEME':
                    end = x + 5
                    #Hide range
                    ida_bytes.add_hidden_range(start,end,'','','',0xFFFFFF)
                    time_waster_slide = False
                else:
                    x += 40
            
