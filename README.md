# UCL_ARRAY30
利用python+pyhook開發的行列30輸入法，肥列輸入法<br>
<br>
<h3>開發動機：</h3>
　　吃飽閒閒覺得人生就是該幫打行列的朋友寫一套輸入法，然後就開始寫了。<br>
<br>
<h3>作者：</h3>
  羽山秋人 (<a target="_blank" href="https://3wa.tw">https://3wa.tw</a>)<br>
<h3>信箱：</h3>
  <a target="_blank" href="mailto:uclliu.3wa@gmail.com">uclliu.3wa@gmail.com</a><br>
<br>
<h3>最初開發日期：</h3>2022-10-13 23:30<br>
<h3>最後更新日期：</h3>2022-10-13 23:30
<br>
<h3>版本：</h3>V 0.01<br>
<br>
<h3>版權：</h3>
　完全免費的 MIT-License
<br>
<h3>下載位置：</h3>
　　1.主程式(0.01 beta版)：<a download="uclarray30.exe" target="_blank" href="https://raw.githubusercontent.com/shadowjohn/UCL_ARRAY30/master/dist/uclarray30.exe">https://raw.githubusercontent.com/shadowjohn/UCL_ARRAY30/master/dist/uclarray30.exe</a><br>　　
	2.字根檔：<a target="_blank" href="https://github.com/shadowjohn/UCL_ARRAY30/array30.cin">https://github.com/shadowjohn/UCL_ARRAY30/array30.cin</a><br>
　　3.歷年版本：<a target="_blank" href="https://github.com/shadowjohn/UCL_ARRAY30/tree/master/RELEASE">歷代版本</a><br>
　　4.同音字庫：<a download="pinyi.txt" target="_blank" href="https://raw.githubusercontent.com/shadowjohn/UCL_LIU/master/dist/pinyi.txt">https://raw.githubusercontent.com/shadowjohn/UCL_LIU/master/dist/pinyi.txt</a><br>
　　5.打字聲音：<a download="pinyi.txt" target="_blank" href="https://raw.githubusercontent.com/shadowjohn/UCL_LIU/master/wavs/wavs.zip">https://raw.githubusercontent.com/shadowjohn/UCL_LIU/master/wavs/wavs.zip</a> 下載後解開，0~9.wav 與 uclarray30.exe 放一起

<br>
<h3>目前肥列輸入法支援的字碼表如下：</h3>
　　1、https://github.com/chinese-opendesktop/cin-tables/blob/master/array30.cin <br>
<br>      
<h3>字碼表說明：</h3>
　　　　街補充
<br>

<h3>使用方法：</h3>
　　1、您可以只下載dist/uclarray30.exe<br>
　　2、將 「array30.cin 或 liu.json」任一種檔案 與 uclarray30.exe 放一起<br>
　　3、執行 uclarray30.exe 即可開始使用<br>
　　4、首次執行，系統會自動將 array30.cin 轉成 array30.json，需要花大概10秒的時間，之後有 array30.json就可以快速開啟。<br>
　　5、未來使用的話，就把uclarray30.exe、作好的字根檔array30.json帶著走，四處都能打肥列輸入法了<br>
　　6、下載 pinyi.txt 與 uclarray30.exe 放一起執行，同音字庫，如「'xxxx」，會出現「待補充...」同音選擇。<br>　　
　　7、pinyi.txt 與 uclarray30.exe 放一起，可以使用「';」切換成「注音模式」，如：ㄈㄟ/，會出現「0肥 1淝 2腓 3萉 4蜰」<br>
　　8、「正常模式」=「,,,unlock」：平常打字用。<br>
　　9、「遊戲模式」=「,,,lock」：玩遊戲時用，如CS:GO，需要按著Shift消音走路。<br>
　　(如果忽然無法打字，也許就是進了「遊戲模式」請按「,,,unlock」解除。)<br>
　　10、「查看目前版本」=「,,,version」 <br>
　　11、「簡體／繁體」模式 「,,,c」「,,,t」 切換<br>
　　12、UI 變窄「,,,s」 <br>
　　13、UI 變寬「,,,l」 <br>
　　14、UI 變大「,,,+」 <br>
　　15、UI 變小「,,,-」 <br>
　　16、uclarray30.ini<br>
　　　　[DEFAULT]<br>
　　　　short_mode = 0  # 是否為「短」版模式， 0 或 1<br>
　　　　zoom = 0.90  # 縮放大小<br>
　　　　send_kind_1_paste = # 如 putty.exe,pcman 遇到此程程式，以 「複製、貼上」 方式出字 <br>
　　　　send_kind_2_big5 = # 如 EWinner.exe 遇到此種程式，以 「big5」 方式出字 <br>
　　　　send_kind_3_noucl = vncviewer.exe,2077 遇到此程式，就無法切換 肥/半、肥/全<br>
　　　　alpha = 1 # 透明度<br>
　　　　y = 950 # 肥列輸入法最後在螢幕 y 軸位置<br>
　　　　x = 1239 # 肥列輸入法最後在螢幕 x 軸位置<br>
　　　　SP = 0 # 是否顯示短根， 0 或 1<br>
　　　　play_sound_enable = 0 # 是否有打字音， 0 或 1<br>
　　　　startup_default_ucl = 1 # 程式啟動時為「肥模式」，0 = 英模式，1 = 肥模式 
　　17、環境設定(強列建議)：<br>
<kbd>
<img src="screenshot/install/1.png"><br>
  <h3>建議可以跟筆者一樣</h3>
</kbd>
<kbd>
<img src="screenshot/install/2.png"><br>
  <h3>安裝一個「ENG語系」，點選【語言喜好設定】」，應該可以在控制台找到。</h3>
</kbd>
<kbd>
<img src="screenshot/l_setting.png"><br>
  <h3>如果找不到，就在搜尋列輸入「語言設定」</h3>
</kbd>
<kbd>
<img src="screenshot/install/3.png"><br>
  <h3>
一、國家與地區，要選「台灣」<br>
二、新增語言：找到「English (United States)」加入，但【中文(台灣)要設為預設值】<br>
三、平常打字時，就選「ENG」打起來就會很順手。<br>
四、Windows更新後，新版的畫面稍有不同，建議可以參考此圖<br>
<img src="screenshot/l_setting_1.png"></br>
Windows 顯示語言：中文（台灣）<br>
在新增完 English (Unitied States) 後，將 English 的順位上移到第一位，才不會一直被注音煩<br>
  </h3>
    17、出字模式選擇：<br>
<kbd>
<h3>感謝網友 klt 回報，提到使用 https://term.ptt.cc/ 無法正常出字，將出字選擇功能作成自定選擇</h3>

</kbd>
  
<br>
<pre>
    (2022-10-13) v0.01 版：
    病毒碼提交掃描：0.01
	待補充

</pre>    

    
<br>
<h3>開發工具：</h3>
  <ul>
    <li>Python 27 (32BIT) : https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi</li>
    <li>pyhook</li>
    <li>pygtk</li>
    <li>pywin32</li>
    <li>pyinstaller 可搭配build.bat製作dist/uclarray30.exe檔</li>
    <li>psutil 用來判斷目前視窗跑什麼，如果是putty、pietty、pcman出字方式要調整</li>
    <li>pyaudio 打字聲音模組</li>
    <li>(Third party) php.py 羽山比較熟php，所以在python裡實作很多php的函式</li>
    <li>(Third party) portalocker.py 防重複執行，會Lock 跟 UCLARRAY30.exe 同目錄下的 UCLARRAY30.lock</li>
    <li>(Third party) SendKeysCtypes.py 可以送出Unicode的SendKeys</li>    
    <li>(Third party) cintojson.py 可以將cin轉成json的檔案，改成支援python2.7的寫法</li>
    <li>(Third party) cin\phone.cin 同音字表參考新酷音的傳統注音表 : https://raw.githubusercontent.com/google/jscin/master/src/tables/phone.cin</li>    
    <li>字碼表亦可參考PIME裡的liu.json</li>
</ul>
<br>
<h3>檔案說明：</h3>
  <ul>
    <li>Python 27 (x86版本):【https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi】</li>
    <li>請設定windows環境變數，在path裡加上 【;c:\Python27;c:\Python27\Scripts】
    <li>pyhook【放在p27目錄，點了安裝即可 p27/pyHook-1.5.1.win32-py2.7.exe】</li>
    <li>pygtk 【放在p27目錄，點了安裝即可 p27/pygtk-all-in-one-2.24.1.win32-py2.7.msi】</li>
    <li>pywin32 【放在p27目錄，點了安裝即可 p27/pywin32-221.win32-py2.7.exe】</li>
    <li>pyaudio 打字音用【pip install pyaudio==0.2.11】</li>    
    <li>pyinstaller 可搭配build.bat製作dist/uclarray30.exe檔【pip install pyinstaller==3.4】</li>
    <li>psutil 用來判斷目前視窗跑什麼，如果是putty、pietty、pcman出字方式是貼上，【pip install psutil==5.8.0】</li>
    <li>configparser config UCLARRAY30.ini 需要用來解 ini 的工具【pip install configparser==4.0.2】</li>
    <li>stts.py 用來簡、繁轉換的工具，感謝臺灣碼農先生</li>
    <li>(Third party) php.py 羽山比較熟php，所以在python裡實作很多php的函式</li>
    <li>(Third party) portalocker.py 防重複執行，會Lock 跟 UCLARRAY30.exe 同目錄下的 UCLARRAY30.lock</li>
    <li>(Third party) SendKeysCtypes.py 可以送出Unicode的SendKeys</li>    
    <li>(Third party) cintojson.py 可以將cin轉成json的檔案，改成支援python2.7的寫法</li>
    <li>(Third party) cin\phone.cin 同音字表參考新酷音的傳統注音表:https://raw.githubusercontent.com/google/jscin/master/src/tables/phone.cin</li>
    <li>(Third party) traybar.py、win32_adapter.py 右下角 trayicon 的作法 # From : https://github.com/Infinidat/infi.systray # From : https://github.com/gevasiliou/PythonTests/blob/master/TrayAllClicksMenu.py</li>
	<li>(Third party) opencc改 協助 ,,,z 簡轉繁的作法 # From : pip2 install opencc、https://github.com/yichen0831/opencc-python</li>
    <li>字碼表亦可參考PIME裡的liu.json</li>
  </ul>
<br>
<h3>自行編譯：</h3>
  <ul>
    <li>1、請下載並安裝python 27 (x86版) 【https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi】</li>
    <li>2、請設定windows環境變數，在path裡加上 【;c:\Python27;c:\Python27\Scripts】</li>
    <li>3、安裝【p27/pyHook-1.5.1.win32-py2.7.exe】</li>
    <li>4、安裝【p27/pygtk-all-in-one-2.24.1.win32-py2.7.msi】</li>
    <li>5、安裝【p27/pywin32-221.win32-py2.7.exe】</li>
    <li>6、至windows cmd，下指令【pip install psutil==5.8.0】</li>
    <li>7、至windows cmd，下指令【pip install pyinstaller==3.4】(如果裝失敗，下面的先裝，並更新 pip 後再回頭裝看看，應該可以成功)</li>
    <li>8、至windows cmd，下指令【pip install configparser==4.0.2】</li>
    <li>9、至windows cmd，下指令【pip install pyaudio==0.2.11】</li>
    <li>10、將下載的行列 array30.cin、dist裡提供的pinyi.txt 與主檔 uclarray30.pyw 放在一起</li>
    <li>11、執行【python uclarray30.pyw】可以跑出程式</li>
    <li>12、編成exe的方法，執行【build.bat】，即可將 uclarray30.exe 編到 dist 目錄下</li>    
    <li>13、pyhook 可以自行編譯，參考心得：【https://3wa.tw/mypaper/index.php?mode=view&id=1709】</li>
    <li>14、如 pyhook 使用自行編譯，可能會遇到【No module named pkgutil】，參考修正心得：【https://3wa.tw/mypaper/index.php?uid=shadow&mode=view&id=1708】</li>
	<li>15、opencc改，如果直接使用 pip install opencc，在 pyinstaller 後無法正常使用，所以羽山直接把 s2t(簡轉繁)、載入 dictionary 檔案的作法，直接改寫到 opencc.py 裡，二個開檔的地方先匯出成文字檔，輸出成檔案(0_json.txt、1_json.txt)看內容是什麼後寫回，這樣 pyinstaller 就能正常了</li>
  </ul>
<br>
<br>
<h3>微軟 Windows Defender 誤判與回報：</h3>
圖片待補充
由於此程式以 pyhook (keyhook) 方式開發，容易被防毒軟體誤判成病毒，已提供微軟進行病毒排除，正常只需要把 Windows Defender 病毒碼更新，啟動時就不會被封鎖了。
<br>

<h3>FAQ：</h3>
1、為何肥列輸入法在啟動後，會有二個執行緒？<br>
圖片待補充
<br>
Ans：<br>
　　第二個執行緒的用途主要是在「英/全」、「肥/半」或「肥/全」模式下，
持續讓肥列一直更新視窗的高度，讓肥列輸入法的視窗，可以置頂，才不會被其他視窗蓋住。<br>
當你切換視窗後，肥列會先被蓋住，但約 1 秒後肥列又會浮上來。<br>
python裡有mostTop可以使用，但不是萬能，幾經測試後還是只能重複呼叫 set_keep_above、set_keep_below 來開關置頂高度，
詳見 uclarray30.pyw function updateGUI()、toAlphaOrNonAlpha() 約在 #3124、 行 #1183 行<br> 
<br>
2、為何有的軟體無法使用肥列輸入法，在該程式視窗時，完全無法觸發肥列輸入法？<br>
Ans：<br>
　　有可能是您當前在使用的視窗，執行的身分是「系統管理員」，嘗試關閉肥列輸入法，然後也使用「系統管理員」執行「肥列輸入法」，就可以正常使用。
<br>
<br>
<h3>ToDo：</h3>
<ul>
  <li>(Done 2022-10-14)1、數字0~9、/\?*; 也是字根</li>
  <li>(Done 2022-10-14)2、當有英文字先，再數字時，此時數字是字根</li>
  <li>(Done 2022-10-14)3、文字選擇，index 從 1 開始</li>
</ul>
<br>
