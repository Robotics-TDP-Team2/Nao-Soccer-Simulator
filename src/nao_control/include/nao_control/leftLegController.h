#ifndef LEFT_LEG_CONTROLLER_H_
#define LEFT_LEG_CONTROLLER_H_

#include "jointsController.h"
#include "dispatchEventService.h"
#include "events_def.h"

class LeftLegController: public JointsController{
public:
    LeftLegController();
    ~LeftLegController();
    void start();
    void stop();
    bool handle(const CEvent* ev);
};

#endif