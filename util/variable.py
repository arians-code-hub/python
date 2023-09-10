class Convert:
    @staticmethod
    def toFloat(val):
        try :
            return float(val)
        except:
            return None
    @staticmethod
    def toInt(val):
        try :
            return int(val)
        except:
            return None

    @staticmethod
    def toNumber(val):
        val = Convert.toInt(val)
        return Convert.toFloat(val) if val is None else val