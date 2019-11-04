.text 
#TODO 4: =============================
# adjust the code to take multiple key presses until 
# key F is pressed. 
#====================================
main: 
		addi $a0, $0,0 		 
		jal init7SegDisp
		li $t6, 0
		j to_display
to_display:
		jal getPressedKey
		add $a0,$v0,$zero
		beq $a0, 15, exit
		jal Num2SegDisp
		j to_display
		#  The program is finished. Exit.
exit: 		li   $v0, 10          # system call for exit
		syscall               # Exit!
.data 
#TODO 1   =================================
# complete the missing seven segment patterns [4-9,A,b,C,d,E,F]
#Hint: You can test your pattern using init7SegDisp
#=========================================
SegBytes: .byte  0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x77, 0x7c, 0x39, 0x5e, 0x79, 0x71

.text
######          Seven segment display help  ############################
 #Byte value at address 0xFFFF0010 : command right seven segment display 
 #Byte value at address 0xFFFF0011 : command left seven segment display 
 # Each bit of these two bytes are connected to segments 
 #(bit 0 for a segment, 1 for b segment and 7 for point 
##=======================================================##
#This procedure initialize the 7-Segment display to 00
init7SegDisp: 
		lui $t0, 0xffff   # load $t0 with base IO address
		addi $t1, $zero, 0x3f  # load seven segment display pattern for 0
		sb $t1, 0x10($t0)  # send 0 to right segment display
		sb $t1, 0x11($t0)  # send 0 to left segment display
		jr $ra


#TODO 3: ==============================================
#   	this procedure displays a single digit number to the seven segment display
#    	Modify it to display up to two digit numbers on the 7-Segment Display
# ======================================================
Num2SegDisp:
		la 	$t0,SegBytes # load the base address of seven-seg pentterns
		add 	$t0,$t0,$a0    # calculate the address of the target pattern
		lb	$t1,0($t0)    # load the target pattern 
		lui 	$t0, 0xffff   # load $t0 with base IO address
		div $t8, $t6, 2
		mfhi $t7
		beqz $t7, right_display
left_display:
		sb $t1, 0x11($t0)
		addi $t6, $t6, 1
		jr $ra
right_display:
		sb $t1, 0x10($t0) # send the target pattern to the 7-segment disp\
		addi $t6, $t6, 1
		jr $ra
		
###################   Hexadecimal keyboard help  #######################
 #Byte value at address 0xFFFF0012 : command row number of hexadecimal keyboard 
 #                                                          (bit 0 to 3) and enable keyboard interrupt (bit 7) 
 #Byte value at address 0xFFFF0014 : receive row and column of the key pressed, 
 #                                                           0 if not key pressed 
 # 0xFFFF0014 byte value is composed of 
 #          - row number (4 bits) and column number (4 bits) 
 
 # To determine the key, the mips program has to 
 #        - set  row bits one by one (i.e., send 1,2,4,8...) at 0xFFFF0012 and then 
 #           reads 0xFFFF0014 to check if a key is pressed in this row
 #======================================================
#TODO 2: ===============================================
#            This procedure captures the pressed key from the first key row and 
#             returns its integer value in $v0 
#             Extend this code to capture any pressed key in any row [0-F] 
#=====================================================
getPressedKey: 
		lui $t0, 0xffff   		# load $t0 with base IO address    
FstRow:	addi $t4,$zero, 1      # set $t4 to 1 to scan the first row
		sb $t4, 0x12($t0)  	# command first row scanning at 0xFFFF0012
		lb  $t2, 0x14($t0)  	# read  0xFFFF0014 for pressed keys 
		bne $t2, $zero, KeyPress # check any pressed keys [zero --> nothing pressed]		
		j  ScdRow  		#scan next row 
ScdRow:
	addi $t4, $zero, 2
	sb $t4, 0x12($t0)
	lb $t2, 0x14($t0)
	bne $t2, $zero, KeyPress
	j ThrdRow
ThrdRow:
	addi $t4, $zero, 4
	sb $t4, 0x12($t0)
	lb $t2, 0x14($t0)
	bne $t2, $zero, KeyPress
	j FrthRow
FrthRow:
	addi $t4, $zero, 8
	sb $t4, 0x12($t0)
	lb $t2, 0x14($t0)
	bne $t2, $zero, KeyPress
	j FstRow
KeyPress:andi $t3,$t2,0xf0    	# Mask 0xFFFF0014 most significant nibble s		
		andi $t2,$t2,0xf      	# Mask 0xFFFF0014 least significant nibble 
		srl   $t3,$t3,4         	# shift $t3 for further processing 
		####  Calculate log $t3   ##########
		add $t5,$zero, $zero		
logt3:	srl   $t3,$t3,1       
		beqz $t3, t5_t3
		addi $t5, $t5, 1
		j  logt3
t5_t3:	move $t3,$t5
	####  Calculate log $t3   ##########
		add $t5,$zero, $zero
logt2:	srl   $t2,$t2,1       
		beqz $t2, t5_t2
		addi $t5, $t5, 1
		j  logt2
t5_t2:	move $t2,$t5
		#addiu $t3,$t3,-1
		## calculate the value of the pressed key ## 
		mul $t2,$t2,4
		add  $v0,$t3,$t2
		jr $ra 
		
