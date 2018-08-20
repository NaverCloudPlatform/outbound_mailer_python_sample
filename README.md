# outbound_mailer_python_sample
Cloud Funtions에서 Outbound Mailer API를 이용해 mail 전달

소스 설명
------

 > __main__.py : cloud functions Action 진입 핸들러
  
 > base_auth_info.py : API 호출하기 위한, 인증 정보 설정
  
 > feedparser.py : python feedparser 라이브러리
  
 > mail_sender.py : Outbound Mailer API 호출
  
 > rss_news_parser.py : feedparser 라이브러리를 이용해, 뉴스 파싱

인증정보 수정
----------

  파일명 : base_auth_info.py

   1) api_key : API Gateway Primary Key
   
   <img width="1248" alt="api_key_primary_key" src="https://user-images.githubusercontent.com/41188783/44326069-7e3fe880-a495-11e8-90ab-1cd04a14b7bf.png">
   
   2) access_key : NCP Access key
   
   3) access_secret : NCP Access secret
   
   ![image](https://user-images.githubusercontent.com/41188783/44326138-ab8c9680-a495-11e8-9db5-553116fd04ec.png)



