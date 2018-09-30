@echo off

set /a nh = %time:~0,2%
set /a nm = %time:~3,2%
set /a ns = %time:~6,2%

set /a sh = 4
set /a sm = 0
set /a ss = 0

set /a ah = %sh% - %nh%
set /a am = %sm% - %nm%
set /a as = %ns% - %ss%

if %ah% lss 0 (%ah% = %ah% + 24)
if %am% lss 0 (%am% = %am% + 60)
if %as% lss 0 (%as% = %as% + 60)

set /a all_s = %ah% * 3600 + %am% * 60 + %as%

shutdown -s -t %all_s%


