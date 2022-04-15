#ifndef COMMON_EVENT_H
#define COMMON_EVENT_H

#include <string>
#include <iostream>
#include "glo_def.h"
using namespace std;


class CEvent
{
public:
    u16 getEid() const {return eid_;};
    void setEid(u16 eid) {eid_ = eid;};
    CEvent(){};
    virtual ~CEvent(){};

private:
    u16 eid_;

protected:
    string content_;
};

#endif