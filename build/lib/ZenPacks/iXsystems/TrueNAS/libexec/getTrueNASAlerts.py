#!/bin/env python

import sys
import requests
import json


RETURN_OK = True
RETURN_KO = False
URL_PATH = 'http://{0}/api/v1.0/system/alert'
SEVERITY_MAPPING = {'CRIT':5, 'WARN':3, 'OK':2}
SEVERITY_PRINTING_MAPPING = {5:'criticalAlerts', 3:'warningAlerts', 2:'infoAlerts', 0:'clearedAlerts'}
EVENT_CLASS = '/TrueNAS/Alert'

class AlertMonitor(object):
  '''
  '''
  def __init__(self, host, login, password):
    '''
    '''
    self.host = host
    self.login = login
    self.password = password
    self.url = URL_PATH.format(self.host)
    self.alerts = []
    self.events = []
    self.statistics = dict([(printName, 0) for sev, printName in SEVERITY_PRINTING_MAPPING.items()])
    return


  def getAlerts(self):
    '''
    '''
    headers = headers={'Content-Type': "application/json"}
    try:
      result = requests.get(self.url, headers = headers, auth=(self.login, self.password))
    except:
      print 'Could not get alerts from server.\n{0}'.format(sys.exc_info())
      sys.exit(1)
    if result.ok:
      try:
        self.alerts = json.loads(result.text)
      except:
        print 'Could not load server response into json object.\n{0}'.format(sys.exc_info())
        sys.exit(1)
    else:
      print 'Server return non OK HTTP response: {0}.'.format(result.status_code)
      sys.exit(1)
    return      


  def parseAlerts(self):
    '''
    '''
    for alert in self.alerts:
      event = {'summary':alert['message'], 'severity':SEVERITY_MAPPING[alert['level']], 'eventKey':alert['id'], 'eventClass':EVENT_CLASS}
      if alert['dismissed']:
        event['severity'] = 0
      self.events.append(event)
    return
  
  def countAlerts(self):
    '''
    '''	
    for event in self.events:
      self.statistics[SEVERITY_PRINTING_MAPPING[event['severity']]] += 1
    return

  def printResult(self):
    '''
    '''
    result = {}
    result['values'] = {'':self.statistics}
    result['events'] = self.events
    print json.dumps(result)
    return

def main():
  '''
  '''
  host = sys.argv[1]
  login = sys.argv[2]  
  password = sys.argv[3] 
  alertMonitor = AlertMonitor(host, login, password)
  alertMonitor.getAlerts()
  alertMonitor.parseAlerts()
  alertMonitor.countAlerts()
  alertMonitor.printResult()
  return

if __name__ == '__main__':
  main()
