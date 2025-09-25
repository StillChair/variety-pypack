
# --- THERMOUC -------------------------------------- #
#                                                     #
# A simple tool made by @StillChair in GitHub         #
# for unit conversion for thermodynamic               #
# properties.                                         #
#                                                     #
#                                                     #
#                                                     #
# --------------------------------------------------- #



def presUC(current_unit, new_unit, inputValue):
    current_unit = current_unit.lower().strip()
    new_unit = new_unit.lower().strip()

    match new_unit:
        case 'mbar':
            match current_unit:
                case 'bar':
                    return inputValue * 1000
                case 'psi':
                    return inputValue * 68.948
                case 'pa':
                    return inputValue / 100
                case 'kpa':
                    return inputValue * 10
                case 'atm':
                    return inputValue * 1013.25
                case 'kg/cm2':
                    return inputValue * 980.665
                case 'mmhg':
                    return inputValue * 1.33322
                case 'mmh2o':
                    return inputValue * 0.0980665
                case 'inhg':
                    return inputValue * 33.8639
                case 'inh2o':
                    return inputValue * 2.49089
                case 'mbar':
                    return inputValue
        
        case 'bar':
            match current_unit:
                case 'mbar':
                    return inputValue / 1000
                case 'psi':
                    return inputValue * 0.0689476
                case 'pa':
                    return inputValue / 100000
                case 'kpa':
                    return inputValue / 100
                case 'atm':
                    return inputValue * 1.01325
                case 'kg/cm2':
                    return inputValue * 0.980665
                case 'mmhg':
                    return inputValue / 750.062
                case 'mmh2o':
                    return inputValue / 10197.2
                case 'inhg':
                    return inputValue / 29.5300
                case 'inh2o':
                    return inputValue / 401.463
                case 'bar':
                    return inputValue
        
        case 'psi':
            match current_unit:
                case 'mbar':
                    return inputValue / 68.948
                case 'bar':
                    return inputValue / 0.0689476
                case 'pa':
                    return inputValue / 6894.76
                case 'kpa':
                    return inputValue / 6.89476
                case 'atm':
                    return inputValue / 0.068046
                case 'kg/cm2':
                    return inputValue / 0.0703070
                case 'mmhg':
                    return inputValue / 0.0193368
                case 'mmh2o':
                    return inputValue / 1.42233
                case 'inhg':
                    return inputValue / 2.03602
                case 'inh2o':
                    return inputValue / 27.6799
                case 'psi':
                    return inputValue
        
        case 'pa':
            match current_unit:
                case 'mbar':
                    return inputValue * 100
                case 'bar':
                    return inputValue * 100000
                case 'psi':
                    return inputValue * 6894.76
                case 'kpa':
                    return inputValue * 1000
                case 'atm':
                    return inputValue * 101325
                case 'kg/cm2':
                    return inputValue * 98066.5
                case 'mmhg':
                    return inputValue * 133.322
                case 'mmh2o':
                    return inputValue * 9.80665
                case 'inhg':
                    return inputValue * 3386.39
                case 'inh2o':
                    return inputValue * 248.089
                case 'pa':
                    return inputValue
        
        case 'kpa':
            match current_unit:
                case 'mbar':
                    return inputValue / 10
                case 'bar':
                    return inputValue * 100
                case 'psi':
                    return inputValue * 6.89476
                case 'pa':
                    return inputValue / 1000
                case 'atm':
                    return inputValue * 101.325
                case 'kg/cm2':
                    return inputValue * 98.0665
                case 'mmhg':
                    return inputValue * 0.133322
                case 'mmh2o':
                    return inputValue * 0.00980665
                case 'inhg':
                    return inputValue * 3.38639
                case 'inh2o':
                    return inputValue * 0.248089
                case 'kpa':
                    return inputValue
        
        case 'atm':
            match current_unit:
                case 'mbar':
                    return inputValue / 1013.25
                case 'bar':
                    return inputValue / 1.01325
                case 'psi':
                    return inputValue * 0.068046
                case 'pa':
                    return inputValue / 101325
                case 'kpa':
                    return inputValue / 101.325
                case 'kg/cm2':
                    return inputValue / 1.03323
                case 'mmhg':
                    return inputValue / 760
                case 'mmh2o':
                    return inputValue / 10332.3
                case 'inhg':
                    return inputValue / 29.9213
                case 'inh2o':
                    return inputValue / 406.782
                case 'atm':
                    return inputValue
        
        case 'kg/cm2':
            match current_unit:
                case 'mbar':
                    return inputValue / 980.665
                case 'bar':
                    return inputValue / 0.980665
                case 'psi':
                    return inputValue * 0.0703070
                case 'pa':
                    return inputValue / 98066.5
                case 'kpa':
                    return inputValue / 98.0665
                case 'atm':
                    return inputValue * 1.03323
                case 'mmhg':
                    return inputValue / 735.559
                case 'mmh2o':
                    return inputValue / 10000
                case 'inhg':
                    return inputValue / 28.959
                case 'inh2o':
                    return inputValue / 393.701
                case 'kg/cm2':
                    return inputValue
        
        case 'mmhg':
            match current_unit:
                case 'mbar':
                    return inputValue / 1.33322
                case 'bar':
                    return inputValue * 750.062
                case 'psi':
                    return inputValue * 51.7149
                case 'pa':
                    return inputValue / 133.322
                case 'kpa':
                    return inputValue / 7.50062
                case 'atm':
                    return inputValue * 760
                case 'kg/cm2':
                    return inputValue * 735.559
                case 'mmh2o':
                    return inputValue / 13.5951
                case 'inhg':
                    return inputValue / 25.4
                case 'inh2o':
                    return inputValue / 1.86832
                case 'mmhg':
                    return inputValue
        
        case 'mmh2o':
            match current_unit:
                case 'mbar':
                    return inputValue / 0.0980665
                case 'bar':
                    return inputValue * 10197.2
                case 'psi':
                    return inputValue / 1.42233
                case 'pa':
                    return inputValue / 9.80665
                case 'kpa':
                    return inputValue * 101.972
                case 'atm':
                    return inputValue * 10332.3
                case 'kg/cm2':
                    return inputValue * 10000
                case 'mmhg':
                    return inputValue * 13.5951
                case 'inhg':
                    return inputValue / 1.86832
                case 'inh2o':
                    return inputValue / 25.4
                case 'mmh2o':
                    return inputValue
        
        case 'inhg':
            match current_unit:
                case 'mbar':
                    return inputValue / 33.8639
                case 'bar':
                    return inputValue * 29.5300
                case 'psi':
                    return inputValue / 2.03602
                case 'pa':
                    return inputValue / 3386.39
                case 'kpa':
                    return inputValue / 3.38639
                case 'atm':
                    return inputValue * 29.9213
                case 'kg/cm2':
                    return inputValue * 28.959
                case 'mmhg':
                    return inputValue * 25.4
                case 'mmh2o':
                    return inputValue * 345.315
                case 'inh2o':
                    return inputValue * 13.5951
                case 'inhg':
                    return inputValue
        
        case 'inh2o':
            match current_unit:
                case 'mbar':
                    return inputValue / 2.49089
                case 'bar':
                    return inputValue * 401.463
                case 'psi':
                    return inputValue / 27.6799
                case 'pa':
                    return inputValue / 248.089
                case 'kpa':
                    return inputValue / 4.01463
                case 'atm':
                    return inputValue * 406.782
                case 'kg/cm2':
                    return inputValue * 393.701
                case 'mmhg':
                    return inputValue * 1.86832
                case 'mmh2o':
                    return inputValue * 25.4
                case 'inhg':
                    return inputValue / 13.5951
                case 'inh2o':
                    return inputValue
                
        case _:
            raise ValueError(f"Could not find unit {new_unit}")
    
def tempUC(current_unit, new_unit, inputValue):
    current_unit = current_unit.lower().strip()
    new_unit = new_unit.lower().strip()

    match new_unit:
        case 'k':
            match current_unit:
                case 'C' | 'c':
                    return inputValue + 273.15
                case 'F' | 'f':
                    return (inputValue - 32) * 5/9 + 273.15
                case 'k':
                    return inputValue
            
        case 'C' | 'c':
            match current_unit:
                case 'k':
                    return inputValue - 273.15
                case 'F' | 'f':
                    return (inputValue - 32) * 5/9
                case 'C' | 'c':
                    return inputValue
            
        case 'F' | 'f':
            match current_unit:
                case 'k':
                    return (inputValue - 273.15) * 9/5 + 32
                case 'C' | 'c':
                    return inputValue * 9/5 + 32
                case 'F' | 'f':
                    return inputValue
        
        case _:
            raise ValueError(f"Could not find unit {new_unit}")

def spenUC(current_unit, new_unit, inputValue, mMass=0.0):
    '''
    Unit conversion for specific energy values.
    Converts units between J/KG, KJ/KG/ MJ/KG, J/MOL, KJ/MOL, MJ/MOL

    Args:
        current_unit (str): String with the source unit of the value. (Ex: J/KG)
        new_unit (str): String with the desired unit of the output value.
        inputValue (int or float): Numeric value that will be converted.
        mMass (int or float): Molar mass in g/mol
    Returns
        (int or float): Input value converted
    '''
    current_unit = current_unit.lower().strip()
    new_unit = new_unit.lower().strip()

    match new_unit:

        ## Mass based
        case 'j/kg':
            match current_unit:
                case 'kj/kg':
                    return inputValue * 1000
                case 'mj/kg':
                    return inputValue * 1000000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # mMass en g/mol -> kg/mol
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return (inputValue * 1000) / (mMass / 1000)
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return (inputValue * 1000000) / (mMass / 1000)
                case 'j/kg':
                    return inputValue
        
        case 'kj/kg':
            match current_unit:
                case 'j/kg':
                    return inputValue / 1000
                case 'mj/kg':
                    return inputValue * 1000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000  # J/mol -> kJ/kg
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # kJ/mol -> kJ/kg
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000)  # MJ/mol -> kJ/kg
                case 'kj/kg':
                    return inputValue
        
        case 'mj/kg':
            match current_unit:
                case 'j/kg':
                    return inputValue / 1000000
                case 'kj/kg':
                    return inputValue / 1000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000000  # J/mol -> MJ/kg
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000  # kJ/mol -> MJ/kg
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # MJ/mol -> MJ/kg
                case 'mj/kg':
                    return inputValue
                
        # Molar based
        case 'j/mol':
            match current_unit:
                case 'kj/mol':
                    return inputValue * 1000
                case 'mj/mol':
                    return inputValue * 1000000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # J/kg -> J/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # kJ/kg -> J/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000000 * (mMass / 1000)  # MJ/kg -> J/mol
                case 'j/mol':
                    return inputValue
        
        case 'kj/mol':
            match current_unit:
                case 'j/mol':
                    return inputValue / 1000
                case 'mj/mol':
                    return inputValue * 1000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # J/kg -> kJ/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # kJ/kg -> kJ/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # MJ/kg -> kJ/mol
                case 'kj/mol':
                    return inputValue
        
        case 'mj/mol':
            match current_unit:
                case 'j/mol':
                    return inputValue / 1000000
                case 'kj/mol':
                    return inputValue / 1000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000000  # J/kg -> MJ/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # kJ/kg -> MJ/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # MJ/kg -> MJ/mol
                case 'mj/mol':
                    return inputValue
                
        case _:
            raise ValueError(f"Could not find unit {new_unit}")

def sphcUC(current_unit, new_unit, inputValue, mMass=0.0):
    '''
    Unit conversion for specific energy values.
    Converts units between J/KGK, KJ/KGK/ MJ/KGK, J/MOLK, KJ/MOLK, MJ/MOLK

    Args:
        current_unit (str): String with the source unit of the value. (Ex: J/KG)
        new_unit (str): String with the desired unit of the output value.
        inputValue (int or float): Numeric value that will be converted.
        mMass (int or float): Molar mass in g/mol
    Returns
        (int or float): Input value converted
    '''
    current_unit = current_unit.lower().strip()
    new_unit = new_unit.lower().strip()

    match new_unit:

        # Mass based
        case 'j/kgk' | 'j/kg.k':
            match current_unit:
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue / 1000
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue / 1000000
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000000
                case 'j/kgk' | 'j/kg.k':
                    return inputValue

        case 'kj/kgk' | 'kj/kg.k':
            match current_unit:
                case 'j/kgk' | 'j/kg.k':
                    return inputValue * 1000
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue / 1000 
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000) 
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) 
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / 1000 / (mMass / 1000) 
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue

        case 'mj/kgk' | 'mj/kg.k':
            match current_unit:
                case 'j/kgk' | 'j/kg.k':
                    return inputValue * 1000000 
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue * 1000 
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000000 / (mMass / 1000)
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000) 
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) 
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue

        # Molar based
        case 'j/molk' | 'j/mol.k':
            match current_unit:
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue / 1000 
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue / 1000000 
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) 
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000 
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000000  
                case 'j/molk' | 'j/mol.k':
                    return inputValue

        case 'kj/molk' | 'kj/mol.k':
            match current_unit:
                case 'j/molk' | 'j/mol.k':
                    return inputValue * 1000 
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue / 1000 
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) 
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000 
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue

        case 'mj/molk' | 'mj/mol.k':
            match current_unit:
                case 'j/molk' | 'j/mol.k':
                    return inputValue * 1000000 
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue * 1000
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000000 * (mMass / 1000)
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000) 
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) 
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue
                
        case _:
            raise ValueError(f"Could not find unit {new_unit}")
        



def unitConv(current_unit, new_unit, inputValue, mMass=0.0):
    """
    General purpose function for converting between different measurement units
    
    Args:
        current_unit (string): Input unit
        new_unit (string): Output unit
        inputValue (float): Value that will be converted
        mMass (float): Molar mass in g/mol
    
    Returns:
        Value converted from input unit to output unit (float)
    """
    
    current_unit = current_unit.lower().strip()
    new_unit = new_unit.lower().strip()
    
    match new_unit:

        # PRESSURE 
        case 'mbar':
            match current_unit:
                case 'bar':
                    return inputValue * 1000
                case 'psi':
                    return inputValue * 68.948
                case 'pa':
                    return inputValue / 100
                case 'kpa':
                    return inputValue * 10
                case 'atm':
                    return inputValue * 1013.25
                case 'kg/cm2':
                    return inputValue * 980.665
                case 'mmhg':
                    return inputValue * 1.33322
                case 'mmh2o':
                    return inputValue * 0.0980665
                case 'inhg':
                    return inputValue * 33.8639
                case 'inh2o':
                    return inputValue * 2.49089
                case 'mbar':
                    return inputValue
        
        case 'bar':
            match current_unit:
                case 'mbar':
                    return inputValue / 1000
                case 'psi':
                    return inputValue * 0.0689476
                case 'pa':
                    return inputValue / 100000
                case 'kpa':
                    return inputValue / 100
                case 'atm':
                    return inputValue * 1.01325
                case 'kg/cm2':
                    return inputValue * 0.980665
                case 'mmhg':
                    return inputValue / 750.062
                case 'mmh2o':
                    return inputValue / 10197.2
                case 'inhg':
                    return inputValue / 29.5300
                case 'inh2o':
                    return inputValue / 401.463
                case 'bar':
                    return inputValue
        
        case 'psi':
            match current_unit:
                case 'mbar':
                    return inputValue / 68.948
                case 'bar':
                    return inputValue / 0.0689476
                case 'pa':
                    return inputValue / 6894.76
                case 'kpa':
                    return inputValue / 6.89476
                case 'atm':
                    return inputValue / 0.068046
                case 'kg/cm2':
                    return inputValue / 0.0703070
                case 'mmhg':
                    return inputValue / 0.0193368
                case 'mmh2o':
                    return inputValue / 1.42233
                case 'inhg':
                    return inputValue / 2.03602
                case 'inh2o':
                    return inputValue / 27.6799
                case 'psi':
                    return inputValue
        
        case 'pa':
            match current_unit:
                case 'mbar':
                    return inputValue * 100
                case 'bar':
                    return inputValue * 100000
                case 'psi':
                    return inputValue * 6894.76
                case 'kpa':
                    return inputValue * 1000
                case 'atm':
                    return inputValue * 101325
                case 'kg/cm2':
                    return inputValue * 98066.5
                case 'mmhg':
                    return inputValue * 133.322
                case 'mmh2o':
                    return inputValue * 9.80665
                case 'inhg':
                    return inputValue * 3386.39
                case 'inh2o':
                    return inputValue * 248.089
                case 'pa':
                    return inputValue
        
        case 'kpa':
            match current_unit:
                case 'mbar':
                    return inputValue / 10
                case 'bar':
                    return inputValue * 100
                case 'psi':
                    return inputValue * 6.89476
                case 'pa':
                    return inputValue / 1000
                case 'atm':
                    return inputValue * 101.325
                case 'kg/cm2':
                    return inputValue * 98.0665
                case 'mmhg':
                    return inputValue * 0.133322
                case 'mmh2o':
                    return inputValue * 0.00980665
                case 'inhg':
                    return inputValue * 3.38639
                case 'inh2o':
                    return inputValue * 0.248089
                case 'kpa':
                    return inputValue
        
        case 'atm':
            match current_unit:
                case 'mbar':
                    return inputValue / 1013.25
                case 'bar':
                    return inputValue / 1.01325
                case 'psi':
                    return inputValue * 0.068046
                case 'pa':
                    return inputValue / 101325
                case 'kpa':
                    return inputValue / 101.325
                case 'kg/cm2':
                    return inputValue / 1.03323
                case 'mmhg':
                    return inputValue / 760
                case 'mmh2o':
                    return inputValue / 10332.3
                case 'inhg':
                    return inputValue / 29.9213
                case 'inh2o':
                    return inputValue / 406.782
                case 'atm':
                    return inputValue
        
        case 'kg/cm2':
            match current_unit:
                case 'mbar':
                    return inputValue / 980.665
                case 'bar':
                    return inputValue / 0.980665
                case 'psi':
                    return inputValue * 0.0703070
                case 'pa':
                    return inputValue / 98066.5
                case 'kpa':
                    return inputValue / 98.0665
                case 'atm':
                    return inputValue * 1.03323
                case 'mmhg':
                    return inputValue / 735.559
                case 'mmh2o':
                    return inputValue / 10000
                case 'inhg':
                    return inputValue / 28.959
                case 'inh2o':
                    return inputValue / 393.701
                case 'kg/cm2':
                    return inputValue
        
        case 'mmhg':
            match current_unit:
                case 'mbar':
                    return inputValue / 1.33322
                case 'bar':
                    return inputValue * 750.062
                case 'psi':
                    return inputValue * 51.7149
                case 'pa':
                    return inputValue / 133.322
                case 'kpa':
                    return inputValue / 7.50062
                case 'atm':
                    return inputValue * 760
                case 'kg/cm2':
                    return inputValue * 735.559
                case 'mmh2o':
                    return inputValue / 13.5951
                case 'inhg':
                    return inputValue / 25.4
                case 'inh2o':
                    return inputValue / 1.86832
                case 'mmhg':
                    return inputValue
        
        case 'mmh2o':
            match current_unit:
                case 'mbar':
                    return inputValue / 0.0980665
                case 'bar':
                    return inputValue * 10197.2
                case 'psi':
                    return inputValue / 1.42233
                case 'pa':
                    return inputValue / 9.80665
                case 'kpa':
                    return inputValue * 101.972
                case 'atm':
                    return inputValue * 10332.3
                case 'kg/cm2':
                    return inputValue * 10000
                case 'mmhg':
                    return inputValue * 13.5951
                case 'inhg':
                    return inputValue / 1.86832
                case 'inh2o':
                    return inputValue / 25.4
                case 'mmh2o':
                    return inputValue
        
        case 'inhg':
            match current_unit:
                case 'mbar':
                    return inputValue / 33.8639
                case 'bar':
                    return inputValue * 29.5300
                case 'psi':
                    return inputValue / 2.03602
                case 'pa':
                    return inputValue / 3386.39
                case 'kpa':
                    return inputValue / 3.38639
                case 'atm':
                    return inputValue * 29.9213
                case 'kg/cm2':
                    return inputValue * 28.959
                case 'mmhg':
                    return inputValue * 25.4
                case 'mmh2o':
                    return inputValue * 345.315
                case 'inh2o':
                    return inputValue * 13.5951
                case 'inhg':
                    return inputValue
        
        case 'inh2o':
            match current_unit:
                case 'mbar':
                    return inputValue / 2.49089
                case 'bar':
                    return inputValue * 401.463
                case 'psi':
                    return inputValue / 27.6799
                case 'pa':
                    return inputValue / 248.089
                case 'kpa':
                    return inputValue / 4.01463
                case 'atm':
                    return inputValue * 406.782
                case 'kg/cm2':
                    return inputValue * 393.701
                case 'mmhg':
                    return inputValue * 1.86832
                case 'mmh2o':
                    return inputValue * 25.4
                case 'inhg':
                    return inputValue / 13.5951
                case 'inh2o':
                    return inputValue
                
        # ============ ENERGÍA ESPECÍFICA ???? (BASE MOLAR) ============
        case '%':
            match current_unit:
                case 'pu':
                    return inputValue * 100
        
        case 'pu':
            match current_unit:
                case '%':
                    return inputValue / 100
        
        # ============ ENERGÍA ESPECÍFICA (BASE MÁSICA) ============
        case 'j/kg':
            match current_unit:
                case 'kj/kg':
                    return inputValue * 1000
                case 'mj/kg':
                    return inputValue * 1000000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # mMass en g/mol -> kg/mol
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return (inputValue * 1000) / (mMass / 1000)
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return (inputValue * 1000000) / (mMass / 1000)
                case 'j/kg':
                    return inputValue
        
        case 'kj/kg':
            match current_unit:
                case 'j/kg':
                    return inputValue / 1000
                case 'mj/kg':
                    return inputValue * 1000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000  # J/mol -> kJ/kg
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # kJ/mol -> kJ/kg
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000)  # MJ/mol -> kJ/kg
                case 'kj/kg':
                    return inputValue
        
        case 'mj/kg':
            match current_unit:
                case 'j/kg':
                    return inputValue / 1000000
                case 'kj/kg':
                    return inputValue / 1000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000000  # J/mol -> MJ/kg
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000  # kJ/mol -> MJ/kg
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # MJ/mol -> MJ/kg
                case 'mj/kg':
                    return inputValue
        
        # ============ ENERGÍA ESPECÍFICA (BASE MOLAR) ============
        case 'j/mol':
            match current_unit:
                case 'kj/mol':
                    return inputValue * 1000
                case 'mj/mol':
                    return inputValue * 1000000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # J/kg -> J/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # kJ/kg -> J/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000000 * (mMass / 1000)  # MJ/kg -> J/mol
                case 'j/mol':
                    return inputValue
        
        case 'kj/mol':
            match current_unit:
                case 'j/mol':
                    return inputValue / 1000
                case 'mj/mol':
                    return inputValue * 1000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # J/kg -> kJ/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # kJ/kg -> kJ/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # MJ/kg -> kJ/mol
                case 'kj/mol':
                    return inputValue
        
        case 'mj/mol':
            match current_unit:
                case 'j/mol':
                    return inputValue / 1000000
                case 'kj/mol':
                    return inputValue / 1000
                case 'j/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000000  # J/kg -> MJ/mol
                case 'kj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # kJ/kg -> MJ/mol
                case 'mj/kg':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # MJ/kg -> MJ/mol
                case 'mj/mol':
                    return inputValue
        
        # ============ TEMPERATURA ============
        case 'k':
            match current_unit:
                case 'C' | 'c':
                    return inputValue + 273.15
                case 'F' | 'f':
                    return (inputValue - 32) * 5/9 + 273.15
                case 'k':
                    return inputValue
        
        case 'C' | 'c':
            match current_unit:
                case 'k':
                    return inputValue - 273.15
                case 'F' | 'f':
                    return (inputValue - 32) * 5/9
                case 'C' | 'c':
                    return inputValue
        
        case 'F' | 'f':
            match current_unit:
                case 'k':
                    return (inputValue - 273.15) * 9/5 + 32
                case 'C' | 'c':
                    return inputValue * 9/5 + 32
                case 'F' | 'f':
                    return inputValue

        # ============ CAPACIDAD CALORÍFICA ESPECÍFICA (BASE MÁSICA) ============
        case 'j/kgk' | 'j/kg.k':
            match current_unit:
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue / 1000  # CORREGIDO: era * 1000
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue / 1000000  # CORREGIDO: era * 1000000
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # mMass en g/mol, convertir a kg/mol
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000  # mMass en g/mol
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000) / 1000000  # mMass en g/mol
                case 'j/kgk' | 'j/kg.k':
                    return inputValue

        case 'kj/kgk' | 'kj/kg.k':
            match current_unit:
                case 'j/kgk' | 'j/kg.k':
                    return inputValue * 1000  # CORREGIDO: era / 1000
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue / 1000  # CORREGIDO: era * 1000
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000)  # mMass en g/mol
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # mMass en g/mol
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / 1000 / (mMass / 1000)  # mMass en g/mol
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue

        case 'mj/kgk' | 'mj/kg.k':
            match current_unit:
                case 'j/kgk' | 'j/kg.k':
                    return inputValue * 1000000  # CORREGIDO: era / 1000000
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue * 1000  # CORREGIDO: era / 1000
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000000 / (mMass / 1000)  # mMass en g/mol
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 / (mMass / 1000)  # mMass en g/mol
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue / (mMass / 1000)  # mMass en g/mol
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue

        # ============ CAPACIDAD CALORÍFICA ESPECÍFICA (BASE MOLAR) ============
        case 'j/molk' | 'j/mol.k':
            match current_unit:
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue / 1000  # CORREGIDO: era * 1000
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue / 1000000  # CORREGIDO: era * 1000000
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # mMass en g/mol, convertir a kg/mol
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # mMass en g/mol
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000000  # mMass en g/mol
                case 'j/molk' | 'j/mol.k':
                    return inputValue

        case 'kj/molk' | 'kj/mol.k':
            match current_unit:
                case 'j/molk' | 'j/mol.k':
                    return inputValue * 1000  # CORREGIDO: era / 1000
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue / 1000  # CORREGIDO: era * 1000
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # mMass en g/mol
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # mMass en g/mol
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000) / 1000  # mMass en g/mol
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue

        case 'mj/molk' | 'mj/mol.k':
            match current_unit:
                case 'j/molk' | 'j/mol.k':
                    return inputValue * 1000000  # CORREGIDO: era / 1000000
                case 'kj/molk' | 'kj/mol.k':
                    return inputValue * 1000  # CORREGIDO: era / 1000
                case 'j/kgk' | 'j/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000000 * (mMass / 1000)  # mMass en g/mol
                case 'kj/kgk' | 'kj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * 1000 * (mMass / 1000)  # mMass en g/mol
                case 'mj/kgk' | 'mj/kg.k':
                    if mMass == 0:
                        raise ValueError("Peso molecular necesario para conversión kg/mol")
                    return inputValue * (mMass / 1000)  # mMass en g/mol
                case 'mj/molk' | 'mj/mol.k':
                    return inputValue
        
        # ============ DENSIDAD ============
        case 'kg/m3':
            match current_unit:
                case 'g/cm3':
                    return inputValue * 1000
                case 'kg/m3':
                    return inputValue
        
        case 'g/cm3':
            match current_unit:
                case 'kg/m3':
                    return inputValue / 1000
                case 'g/cm3':
                    return inputValue
        
        # ============ PESO MOLECULAR ============
        case 'g/mol':
            match current_unit:
                case 'kg/mol':
                    return inputValue * 1000
                case 'g/mol':
                    return inputValue
        
        case 'kg/mol':
            match current_unit:
                case 'g/mol':
                    return inputValue / 1000
                case 'kg/mol':
                    return inputValue
        
        # ============ VELOCIDAD ============
        case 'm/s':
            match current_unit:
                case 'm/s':
                    return inputValue
        
        # ============ VISCOSIDAD DINÁMICA ============
        case 'pa.s':
            match current_unit:
                case 'pa.s':
                    return inputValue
        
        # ============ PARA COOLPROP (casos especiales) ============
        case 'default_coolprop':
            match current_unit:
                case 'F' | 'f':
                    return (inputValue - 32) * 5/9 + 273.15
                case 'C' | 'c':
                    return inputValue + 273.15
                case 'k':
                    return inputValue
                case 'mbar':
                    return inputValue * 100
                case 'bar':
                    return inputValue * 100000
                case 'psi':
                    return inputValue * 6894.76
                case 'kpa':
                    return inputValue * 1000
                case 'atm':
                    return inputValue * 101325
                case 'kg/cm2':
                    return inputValue * 98066.5
                case 'mmhg':
                    return inputValue * 133.322
                case 'mmh2o':
                    return inputValue * 9.80665
                case 'inhg':
                    return inputValue * 3386.39
                case 'inh2o':
                    return inputValue * 248.089
                case 'pa':
                    return inputValue
                case 'kj/kg':
                    return inputValue * 1000
                case 'mj/kg':
                    return inputValue * 1000000
                case 'j/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * mMass
                case 'kj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 * mMass
                case 'mj/mol':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000000 * mMass
                case 'j/kg':
                    return inputValue
                case 'kj/kgk' | 'kj/kg.k':
                    return inputValue * 1000
                case 'mj/kgk' | 'mj/kg.k':
                    return inputValue * 1000000
                case 'j/molk' | 'j/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * mMass
                case 'kj/molk' | 'kj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000 * mMass
                case 'mj/molk' | 'mj/mol.k':
                    if mMass == 0:
                        raise ValueError("This conversion requires a molar mass input")
                    return inputValue * 1000000 * mMass
                case 'j/kgk' | 'j/kg.k':
                    return inputValue
                case 'g/cm3':
                    return inputValue * 1000
                case 'kg/m3':
                    return inputValue

                case _:
                    return inputValue
        
        # Caso por defecto - si no encuentra conversión, devolver el valor original
        case _:
            print(f"Advertencia: No se encontró conversión de {current_unit} a {new_unit}")
            return inputValue


def example():
    '''
    Example execution of functions inside the code
    '''
    print("--- EXAMPLE ---")
    
    # Temperature conversion
    print(f"25°C to K: {tempUC('c', 'k', 25):.2f} K")
    print(f"77°F to °C: {unitConv('f', 'c', 77):.2f} °C")
    
    # Pressure conversion
    print(f"1 bar to psi: {presUC('bar', 'psi', 1):.2f} psi")
    print(f"14.7 psi to kPa: {unitConv('psi', 'kpa', 14.7):.2f} kPa")
    
    # Specific Energy conversion (with molar mass)
    molarMass = 18.015  # Water molar mass in grams per mol
    print(f"1000 J/kg to kJ/mol (H2O): {spenUC('j/kg', 'kj/mol', 1000, molarMass):.4f} kJ/mol")
    
    # Density conversion
    print(f"1 g/cm³ to kg/m³: {unitConv('g/cm3', 'kg/m3', 1):.0f} kg/m³")


    example()



