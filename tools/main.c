/*
 * Copyright (c) 2009, Zilogic Systems <code@zilogic.com>
 *
 * Permission to use, copy, modify, and/or distribute this software
 * for any purpose with or without fee is hereby granted, provided
 * that the above copyright notice and this permission notice appear
 * in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
 * WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
 * AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
 * CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
 * OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
 * NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
 * CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#include <p89v51rd2.h>
/*
* LED1 is connected to P1.4
* LED2 is connected to P1.5
*/

#define LED1 P1_4
#define LED2 P1_5

/* delay value between LEDs ON and OFF */
#define BLINKING_DELAY	30000

main()
{
	int i;
	/* Initaialize the state of the leds */
	LED1 = 1;
	LED2 = 0;
	while (1) {
		LED1 = !LED1;
		LED2 = !LED2;
		/* Delay loop */
		for (i = 0; i < BLINKING_DELAY; i++);
	}
}
