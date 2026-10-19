class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleet = [] #LIFO
        pairs = sorted(zip(position,speed), reverse =True)
        for p,s in pairs:
            car_steps_to_target = (target - p) / s
            if not carFleet or car_steps_to_target > carFleet[-1]:
                carFleet.append(car_steps_to_target)
        print(carFleet)
        return len(carFleet)
                    
