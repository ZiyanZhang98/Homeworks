.data
	inputStr: .space 20
	str2float: .float
	ask: .asciiz "$ Enter a real number:"
	sign: .asciiz "$ The sign bit of your number is: "
	error: .asciiz "invalid input! "
	exponent_bin: .asciiz "\n$ The exponent of your number is: exponentBinary: "
	f_hex: .asciiz"\tfractionHex: "
	display_hex: .asciiz "\texponentHex: "
	f_bin: .asciiz "\n$The fraction of your number is: fractionBinary: "
	space: .asciiz " "
	hex: .asciiz "			"
	to_hex: .asciiz " "
	
.text
.globl main
main:
	li $v0, 4
	la $a0, ask
	syscall
	
	li $v0, 8
	la $a0, inputStr
	li $a1, 20
	syscall
	
	la $t0, inputStr
	li $t1, 0
	
get_len:
	lb $t2, 0($t0)
	beqz $t2, end_count
	addi $t0, $t0, 1
	addi $t3, $t3, 1
	j get_len
end_count:
	addi $t3, $t3, -1	# $t3 stores the length of the string
	
convert_to_int:
	lb $t0, inputStr($t1)
	beq $t0, 45, negative	# 45 represents  '-' in ascii table
	bne $t0, 46, push
	addi $t1, $t1, 1
	add $t5, $t1, $zero	# $t5 stores the R part
	j convert_to_int
negative:
	add $t3, $t3, -1	# decrease length by 1
	addi $t1, $t1, 1	# get rid of  '-' operator
	li $t9, 1		# set $t9 as a negative flag, when a '-' is read, set flag to 1
	j convert_to_int
push:				# push every single number into stack
	blt $t0,48,r_error
	bgt $t0, 57, r_error
	addi $t0, $t0, -48
	addi $t1, $t1, 1
	addi $sp, $sp, -4
	sw $t0, 0($sp)
	beq $t3, $t1, end_push
	j convert_to_int
end_push:
	li $t1, 0
	li $t2, 1
	j pop
	
pop:				# read from the stack
	lw $t0, 0($sp)
	addi $sp, $sp, 4
	mul $t0, $t0, $t2
	add $t4, $t4, $t0
	mul $t2, $t2, 10
	addi $t1, $t1, 1
	beq $t1, $t3, end_pop
	j pop
end_pop:
	li $t2, 10
	sub $t5, $t3, $t5

	mtc1 $t4, $f0
	cvt.s.w $f0, $f0
	mtc1 $t2, $f1
	cvt.s.w $f1, $f1
	
to_float:			# convert to float
	div.s $f0, $f0, $f1
	addi $t5, $t5, -1
	beqz $t5, check
	j to_float

check:
	beqz $t9, store_float
	neg.s $f0, $f0
	
store_float:
	mtc1 $t4, $f3
	cvt.s.w $f3, $f3
	s.s $f0, str2float
	
	addi $sp, $sp, -4
	s.s $f0, 0($sp)
	lw $t5, 0($sp)
	addi $sp, $sp, 4
	li $t1, 32
to_binary:
	beqz $t1, print_sign
	addi $t1, $t1, -1
	divu $t5, $t5, 2
	mfhi $t2
	addi $sp, $sp, -4
	sw $t2, 0($sp)
	j to_binary

print_sign:
	li $v0, 4
	la $a0, sign
	syscall
	
	li $v0, 1
	lw $a0, 0($sp)
	syscall
	
	addi $sp, $sp, 4

print_exponent_string:
	li $v0, 4
	la $a0, exponent_bin
	syscall
	
	li $t0, 0
	li $t1, 8
	li $t5, 0
	li $t6, 0
	
print_binary_exponent:
	mul $t0, $t0, 2
	beqz $t1, print_hex_string
	addi $t1, $t1, -1
	lw $t7, 0($sp)
	add $t0, $t0, $t7
	addi $sp, $sp, 4
	li $v0,1 
	move $a0, $t7
	syscall
	div $t2, $t1, 4
	mfhi $t3
	beqz $t3, print_space
	j print_binary_exponent
	
print_space:
	li $v0, 4
	la $a0, space
	syscall
	
	blt $t0, 10, convert_to_hex
	addi $t0, $t0, 7
convert_to_hex:
	addi $t0, $t0, 48
	sb $t0, hex($t5)
	li $t0, 0
	addi $t5, $t5, 1
	j print_binary_exponent
	
print_hex_string:
	li $v0, 4
	la $a0, display_hex
	syscall
print_hex_exponent:
	lb $t8, hex($t6)
	sb $t8, to_hex
	li $v0, 4
	la $a0, to_hex
	addi $t6, $t6, 1
	syscall
	beq $t5, $t6, end_exponent
	j print_hex_exponent

end_exponent:
	li $t0, 0
	li $t1, 23
	li $t7, 0
	li $v0, 4
	la $a0, f_bin
	syscall

print_fraction:
	mul $t0, $t0, 2
	beqz $t1, print_hex_string2
	addi $t1, $t1, -1
	lw $t7, 0($sp)
	add $t0, $t0, $t7
	addi $sp, $sp, 4
	li $v0,1 
	move $a0, $t7
	syscall
	div $t2, $t1, 4
	mfhi $t3
	beqz $t3, print_space2
	j print_fraction
	
print_space2:
	li $v0, 4
	la $a0, space
	syscall
	
	blt $t0, 10, convert_to_hex2
	addi $t0, $t0, 7

convert_to_hex2:
	addi $t0, $t0, 48
	sb $t0, hex($t5)
	li $t0, 0
	addi $t5, $t5, 1
	j print_fraction
	
print_hex_string2:
	li $v0, 4
	la $a0, f_hex
	syscall
	
push_hex:
	lb $t1, hex($t6)
	addi $sp, $sp, -4
	sw $t1, 0($sp)
	
	li $v0, 4
	la $a0, 0($sp)
	syscall
	
	div $t2, $t6, 2
	mfhi $t3
	beq  $t3, 1, call_space
	
	addi $t6, $t6, 1
	beq $t6, $t5, end
	j push_hex
	
call_space:
	li $v0, 4
	la $a0, space
	syscall
	
	add $t6, $t6, 1
	beq $t6, $t5, end
	j push_hex

r_error:
	li $v0, 4
	la $a0, error
	syscall
end:
	





		
