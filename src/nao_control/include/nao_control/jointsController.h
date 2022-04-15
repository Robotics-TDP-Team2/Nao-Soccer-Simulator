#ifndef JOINTS_CONTROLLER_H_
#define JOINTS_CONTROLLER_H_
#include "event.h"
#include <iostream>


class JointsController
{
public:
    virtual bool handle(const CEvent* ev) = 0;
    virtual ~JointsController() {};
    JointsController(){};
};

#endif