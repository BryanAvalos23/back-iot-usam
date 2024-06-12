class Config:
  SECRET_KEY = "UniversidadsalvadorenaalbertomasferrerIoTInvestigacion"

class DevelopmentConfig(Config):
  DEBUG = True

config = {
  'development': DevelopmentConfig
}