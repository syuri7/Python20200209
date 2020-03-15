@echo off

setlocal enableDelayedExpansion 

rem bat 파일을 실행할 때는 파일 저장 형식이 중요합니다.
rem bat 파일을 utf-8 방식으로 저장하면 실행이 안될 수도 있음. 
rem bat 파일을 저장할 때는 반드시 ASCII 방식으로 저장해야 한다. 
rem
rem bat 파일을 윈도우 서비스로 등록하는 방법은 구글 검색한다. 
rem https://potensj.tistory.com/108

SET ROOTDIR=%CD%

:CheckOS
IF EXIST "%PROGRAMFILES(X86)%" (set BITS=64) ELSE (set BITS=32)



rem @@@@@@@@@@@@@@@@@@@@@
rem step 1. PYTHONPATH 확인
rem @@@@@@@@@@@@@@@@@@@@@

echo %PYTHONPATH%

rem @@@@@@@@@@@@@@@@@@@@@
rem step 2. 현재 디렉토리 확인
rem @@@@@@@@@@@@@@@@@@@@@
echo %ROOTDIR%
echo[ 

rem %PYTHONPATH%\python.exe %ROOTDIR%\py소스.py

python.exe %ROOTDIR%\배치.py  





PAUSE
EXIT


