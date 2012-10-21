#include <stdio.h>
#include "ogg/ogg.h"

int main () {
  ogg_stream_state os;
  int serialno = 69;
  return ogg_stream_init(&os, serialno);
}
