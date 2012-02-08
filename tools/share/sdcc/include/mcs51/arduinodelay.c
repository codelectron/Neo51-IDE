
#ifndef __ARDDELAY__
#define __ARDDELAY__

#ifndef __DELAY_H__
#endif

void Delayms(unsigned long milliseconde)
{
	unsigned long i;
	
	for (i=0;i<milliseconde;i++);
}

void Delayus(int microsecondes)
{
	unsigned int i;
	
	for (i=0;i<microsecondes;i++);
}

#endif
