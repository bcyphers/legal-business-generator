# Totally Legal Business Generator v. 1.0
import random
import re

strings = ['A company that uses %data_types data from %demographics to %purposes',
           'A company that sells %data_types data about %demographics to %entities',
           'A company that collects %data_types data about %demographics for %law_enforcement',
           'A company that buys %data_types data about %demographics from %other_businesses']

dic = {
    'data_types': ['location', 'credit', 'employment history',
                  'personality profile', 're-identified health',
                  'internet browsing', 'dating app usage',
                  'online purchase', 'retail purchase history',
                  'driving behavior', 'pornography viewing history', 'DNA'],
    'demographics': ['pregnant women', 'single gay men', 'young democrats',
                    'church-going catholics', 'people with bad credit',
                    'people with mental health issues', 'conspiracy theorists',
                    'everyone', 'the unemployed', 'crazy cat people', 'teenagers',
                    'people with gambling addictions', 'the homeless',
                    'single mothers', 'lonely men', 'undocumented immigrants',
                     'likely voters'],
    'purposes': ['target ads', 'detect ToS violations', 'augment customer profiles',
                'identify upsell targets', 'train predictive models',
                'identify market inefficiencies', 'monitor competing businesses',
                'perform A/B testing', 'make political predictions',
                'forecast the price of oil'],
    'entities': ['private investigators', 'reposession agencies', 'debt collectors',
                'advertisers', 'political campaigns', 'local governments',
                'hedge funds', 'subprime lenders', 'the Church of Scientology',
                'foreign governments', 'drug companies', 'Big Tobacco',
                'used car dealerships', 'landlords', 'the Republican Party'],
    'other_businesses': ['grocery stores', 'car companies', 'gyms',
                        'failing startups', 'retailers', 'TV manufacturers',
                        'IoT companies', 'independent app developers',
                        'mommy blogs', 'electronic billboard operators',
                        'real estate agents', 'menstruation tracking apps',
                        'weather apps'],
    'law_enforcement': ['the FBI', 'ICE', 'INTERPOL', 'state and local police']
}

company = random.choice(strings)
for l in dic:
    company = re.sub('(?<=%)' + l, random.choice(dic[l]), company)

company = ''.join(company.split('%'))

print(company)
