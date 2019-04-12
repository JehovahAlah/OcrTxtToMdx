#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bsld.py
#  
#  Copyright 2019 Jehovah <Jehovah@DESKTOP-HGTHPQC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  






with open('D:\ldresult.txt','a',encoding='utf-8') as ldresult_obj:
	with open('D:\citou.txt',encoding='utf-8') as citou_obj:
		with open('D:\ld.txt',encoding='utf-8') as ld_obj:
			for row in citou_obj:
			
				for line in ld_obj:
					
					row=str(row)
					row=row.strip('\r\n')
					line=str(line)					if line.startswith(row):						ldresult_obj.write('</>\n')						ldresult_obj.write(row)						ldresult_obj.write('\n')						ldresult_obj.write(line)						break					else:						ldresult_obj.write(line)			         		    							
							
						
					    
				    
				
		
		
		
		
		
		
		
		
    
