# Base component constants
NAME = "Smart Autotune Thermostat"
DOMAIN = "sat"
VERSION = "3.0.x"
CLIMATE = "climate"
COORDINATOR = "coordinator"
CONFIG_STORE = "config_store"

MODE_FAKE = "fake"
MODE_MQTT = "mqtt"
MODE_SWITCH = "switch"
MODE_SERIAL = "serial"
MODE_SIMULATOR = "simulator"

DEADBAND = 0.1
HEATER_STARTUP_TIMEFRAME = 180

MINIMUM_SETPOINT = 10
MINIMUM_RELATIVE_MOD = 0
MAXIMUM_RELATIVE_MOD = 100

MAX_BOILER_TEMPERATURE_AGE = 60
OVERSHOOT_PROTECTION_SETPOINT = 75
OVERSHOOT_PROTECTION_REQUIRED_DATASET = 40

# Configuration and options
CONF_MODE = "mode"
CONF_NAME = "name"
CONF_DEVICE = "device"
CONF_SIMULATED_HEATING = "simulated_heating"
CONF_SIMULATED_COOLING = "simulated_cooling"
CONF_SIMULATED_WARMING_UP = "simulated_warming_up"
CONF_MINIMUM_SETPOINT = "minimum_setpoint"
CONF_MAXIMUM_SETPOINT = "maximum_setpoint"
CONF_MAXIMUM_RELATIVE_MODULATION = "maximum_relative_modulation"
CONF_SECONDARY_CLIMATES = "secondary_climates"
CONF_MQTT_TOPIC = "mqtt_topic"
CONF_MAIN_CLIMATES = "main_climates"
CONF_WINDOW_SENSORS = "window_sensors"
CONF_SYNC_WITH_THERMOSTAT = "sync_with_thermostat"
CONF_WINDOW_MINIMUM_OPEN_TIME = "window_minimum_open_time"
CONF_THERMAL_COMFORT = "thermal_comfort"
CONF_SIMULATION = "simulation"
CONF_INTEGRAL = "integral"
CONF_DERIVATIVE = "derivative"
CONF_PROPORTIONAL = "proportional"
CONF_DUTY_CYCLE = "duty_cycle"
CONF_SAMPLE_TIME = "sample_time"
CONF_AUTOMATIC_GAINS = "automatic_gains"
CONF_AUTOMATIC_DUTY_CYCLE = "automatic_duty_cycle"
CONF_AUTOMATIC_GAINS_VALUE = "automatic_gains_value"
CONF_DERIVATIVE_TIME_WEIGHT = "derivative_time_weight"
CONF_CLIMATE_VALVE_OFFSET = "climate_valve_offset"
CONF_SENSOR_MAX_VALUE_AGE = "sensor_max_value_age"
CONF_OVERSHOOT_PROTECTION = "overshoot_protection"
CONF_SYNC_CLIMATES_WITH_PRESET = "sync_climates_with_preset"
CONF_FORCE_PULSE_WIDTH_MODULATION = "force_pulse_width_modulation"
CONF_TARGET_TEMPERATURE_STEP = "target_temperature_step"
CONF_INSIDE_SENSOR_ENTITY_ID = "inside_sensor_entity_id"
CONF_OUTSIDE_SENSOR_ENTITY_ID = "outside_sensor_entity_id"
CONF_HUMIDITY_SENSOR_ENTITY_ID = "humidity_sensor_entity_id"
CONF_DYNAMIC_MINIMUM_SETPOINT = "dynamic_minimum_setpoint"
CONF_MINIMUM_SETPOINT_ADJUSTMENT_FACTOR = "minimum_setpoint_adjustment_factor"

CONF_HEATING_SYSTEM = "heating_system"
CONF_HEATING_CURVE_VERSION = "heating_curve_version"
CONF_HEATING_CURVE_COEFFICIENT = "heating_curve_coefficient"

CONF_PID_CONTROLLER_VERSION = "pid_controller_version"

CONF_MINIMUM_CONSUMPTION = "minimum_consumption"
CONF_MAXIMUM_CONSUMPTION = "maximum_consumption"

CONF_AWAY_TEMPERATURE = "away_temperature"
CONF_HOME_TEMPERATURE = "home_temperature"
CONF_SLEEP_TEMPERATURE = "sleep_temperature"
CONF_COMFORT_TEMPERATURE = "comfort_temperature"
CONF_ACTIVITY_TEMPERATURE = "activity_temperature"

HEATING_SYSTEM_UNKNOWN = "unknown"
HEATING_SYSTEM_HEAT_PUMP = "heat_pump"
HEATING_SYSTEM_RADIATORS = "radiators"
HEATING_SYSTEM_UNDERFLOOR = "underfloor"

OPTIONS_DEFAULTS = {
    CONF_MODE: MODE_SERIAL,
    CONF_PROPORTIONAL: "45",
    CONF_INTEGRAL: "0",
    CONF_DERIVATIVE: "6000",

    CONF_AUTOMATIC_GAINS: True,
    CONF_AUTOMATIC_DUTY_CYCLE: True,
    CONF_AUTOMATIC_GAINS_VALUE: 5.0,
    CONF_DERIVATIVE_TIME_WEIGHT: 6.0,
    CONF_OVERSHOOT_PROTECTION: False,
    CONF_DYNAMIC_MINIMUM_SETPOINT: False,
    CONF_MINIMUM_SETPOINT_ADJUSTMENT_FACTOR: 0.2,

    CONF_SECONDARY_CLIMATES: [],
    CONF_MAIN_CLIMATES: [],
    CONF_SIMULATION: False,
    CONF_WINDOW_SENSORS: [],
    CONF_THERMAL_COMFORT: False,
    CONF_HUMIDITY_SENSOR_ENTITY_ID: None,
    CONF_SYNC_WITH_THERMOSTAT: False,
    CONF_SYNC_CLIMATES_WITH_PRESET: False,

    CONF_SIMULATED_HEATING: 20,
    CONF_SIMULATED_COOLING: 5,

    CONF_MINIMUM_SETPOINT: 10,
    CONF_MAXIMUM_RELATIVE_MODULATION: 100,
    CONF_FORCE_PULSE_WIDTH_MODULATION: False,

    CONF_MINIMUM_CONSUMPTION: 0,
    CONF_MAXIMUM_CONSUMPTION: 0,

    CONF_MQTT_TOPIC: "OTGW",
    CONF_DUTY_CYCLE: "00:13:00",
    CONF_SAMPLE_TIME: "00:01:00",
    CONF_CLIMATE_VALVE_OFFSET: 0,
    CONF_TARGET_TEMPERATURE_STEP: 0.5,
    CONF_SENSOR_MAX_VALUE_AGE: "06:00:00",
    CONF_SIMULATED_WARMING_UP: "00:00:15",
    CONF_WINDOW_MINIMUM_OPEN_TIME: "00:00:15",

    CONF_ACTIVITY_TEMPERATURE: 10,
    CONF_AWAY_TEMPERATURE: 10,
    CONF_HOME_TEMPERATURE: 18,
    CONF_SLEEP_TEMPERATURE: 15,
    CONF_COMFORT_TEMPERATURE: 20,

    CONF_HEATING_CURVE_VERSION: 3,
    CONF_HEATING_CURVE_COEFFICIENT: 1.0,
    CONF_HEATING_SYSTEM: HEATING_SYSTEM_RADIATORS,

    CONF_PID_CONTROLLER_VERSION: 2,
}

# Storage
STORAGE_OVERSHOOT_PROTECTION_VALUE = "overshoot_protection_value"

# Services
SERVICE_RESET_INTEGRAL = "reset_integral"
SERVICE_SET_OVERSHOOT_PROTECTION_VALUE = "set_overshoot_protection_value"
SERVICE_START_OVERSHOOT_PROTECTION_CALCULATION = "start_overshoot_protection_calculation"

# Config steps
STEP_SETUP_GATEWAY = "gateway"
STEP_SETUP_SENSORS = "sensors"
