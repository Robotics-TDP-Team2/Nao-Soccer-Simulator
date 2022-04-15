#ifndef RIGHT_LEG_CONTROLLER_H_
#define RIGHT_LEG_CONTROLLER_H_


#include "jointsController.h"
#include "dispatchEventService.h"
#include "events_def.h"

class RightLegController: public JointsController{
public:
    RightLegController();
    ~RightLegController();
    void start();
    void stop();
    bool handle(const CEvent* ev);
};


#endif