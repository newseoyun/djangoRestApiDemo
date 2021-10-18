from django.test import TestCase, Client

# Create your tests here.


from product.models import Person

# 설정한 엔드포인트 경로를 통해 함수를 호출. request나 http와 비슷한 일
client = Client() 

# 테스트 케이스를 만들 때는 항상 TestCase() 객체를 상속받아 새로운 테스트 클래스를 생성한다.
class SignupTest(TestCase): 
	# 테스트 함수는 test_ 를 붙여주어야 테스트 함수로 인식한다.
    def test_signup_post_success(self): 
	# 테스트를 위해 User Model의 Field값에 임의의 데이터를 저장한다.
        data = {
            'first_name' : 'hi',
            'last_name'  : 'hello',
        }
	# post 함수에 대한 테스트이기 때문에 post로 작성을 한다.
	# json.dumps 는 python 객체를 json string으로 변환하는 역할을 하는 함수
	# content_type에서 형식을 json 형식으로 지정해줌
        response = client.post('/persons', json.dumps(data), content_type = 'application/json')
				
	# 반환되는 status_code와 message가 같은지 비교하여 같을 경우 테스트에서 OK를 띄워준다.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "message" : "SUCCESS"
        })