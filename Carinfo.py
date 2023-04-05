class Car:
    def __init__ (self, make, model): # car 클래스 생성자
        self.make = make # make 인스턴스 변수 생성 및 초기화
        self.model = model # model 인스턴스 변수 생성 및 초기화
        self.odometer_reading = 0# odometer_reading 인스턴스 변수 생성 및 초기화

    def get_descriptive_name(self): # 자동차 정보를 반환하는 에소드
        long_name = f"{self.make} {self. model}" # 자동차 정보 생성
        return long_name.title() # 자동차 정보 반환

    def read_odometer(self): # 주행거리를 출럭하는 에소드
        print(f"This car has {self. odometer_reading} miles on it.") # 주행거리 출력

    def update_odometer(self, mileage): # 주행거리를 의데이트하는 메소드
        if mileage >= self.odometer_reading: # 주행거리가 증가하는 경우
            self.odometer_reading = mileage # 주행거리 억데이트
        else: # 주행거리가 감소하는 경우
            print("You can't roll back an odometer!") # 주행거리 감소 불가능 메시지 출력

    def increment_odometer(self, miles): # 주행거리를 증가시키는 메소드
        self.odometer_reading += miles # 주행거리 중가
        
my_new_car = Car('audi', 'a4') # car 클래스의 인스턴스 생성

print(my_new_car.get_descriptive_name()) # 자동차 정보 출력

my_new_car.update_odometer(20) # 주행거리 업데이트
my_new_car.read_odometer() # 주행거리 출력
