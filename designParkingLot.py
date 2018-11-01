PARKING_EMPTY = False
PARKING_FULL = False

VECHICLE_TYPES = ['bike','compact','sedan','truck']

class ParkingLot:
    def __init__(self,slot_id,status,parking_type,vehicle):
        """

        :param slot_id: Parking Slot ID Number
        :param status: EMPTY or OCCUPIED
        :param parking_type: BIKE or CAR
        :param vehicle: CAR
        """
        self.slot_id = slot_id
        self.status = status
        self.parking_type = parking_type
        self.vehicle = vehicle

    def parkVehicle(self,vehicle):
        

    def findEmptySlot(self):
        pass

class Floor:
    def __init__(self,floor_id,floorNum,floorName,parkingSlots):
        self.floor_id = floor_id
        self.floorNum = floorNum
        self.floorName = floorName
        self.parkingSlots = parkingSlots

    def emptyFloor(self):
        pass

class Vehicle:
    def __init__(self,vehicle):
        self.vehicle  = vehicle
        self.vehicleType = ''

    def getvehicleType(self):
        if self.vehicle == 'hatchback':
            self.vehicleType = 'compact'
        elif self.vehicle == 'bike':
            self.vehicleType = 'bike'
        elif self.vehicle == 'sedan':
            self.vehicleType = 'sedan'

class ParkingDetails:
    def __init__(self,vehicle,entryTime,exitTime):
        pass
    def CalcParkingFees(self):
        pass

class SlotSize:
    """
    Small => Bike Compact
    Medium => Bike, Compact, Sedan
    Large => Bike, Compact, Sedan, truck
    """
    def __init__(self,vehicleType):
        self.slotSize = ''
        self.vehicleType = vehicleType

    def getSlotSize(self):
        if self.vehicleType in ['bike','compact']:
            self.slotSize = 'small'
        elif self.vehicleType in ['bike','compact','sedan']:
            self.slotSize = 'medium'
        elif self.vehicleType in ['bike','compact','sedan','truck']:
            self.slotSize = 'large'
        return self.slotSize

class FareController:
    def __init__(self):
        self.vehicleParkingDetails = {}

    def onVehicleEntry(self):
        pass
    def onVehicleExit(self):
        pass
    def getFare(self):
        pass